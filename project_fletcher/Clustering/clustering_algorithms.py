
# coding: utf-8

import pandas as pd
import numpy as np

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.decomposition import NMF, TruncatedSVD
from sklearn.cluster import KMeans, DBSCAN, SpectralClustering, MeanShift, estimate_bandwidth
from sklearn.manifold import TSNE

from sklearn.metrics.pairwise import cosine_similarity

import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use("seaborn")

# from itertools import cycle
# from sklearn import datasets
# import logging
# from sklearn.preprocessing import StandardScaler
# from sklearn.metrics import silhouette_score


class clustering_pipeline:
    def __init__(self, vectorizer, n_components, reducer):
        self.vectorizer = vectorizer
        self.n_dim = n_components
        self.reducer = reducer(n_components)

    def fit(self, text):
        self.vectorizer.fit(text)
        self.vector_data = self.vectorizer.fit_transform(text)
        self.topic_data = self.reducer.fit_transform(self.vector_data)
        self.texts = text

    def tsne(self, n_components, perplexity):
        tsne = TSNE(n_components = n_components, perplexity = perplexity)
        plt.figure(dpi=300)
        vector_tsne = tsne.fit_transform(self.topic_data)
        sns.scatterplot(vector_tsne[:, 0], vector_tsne[:, 1],hue=self.labels_, alpha=0.5, size = 0.5,
                        palette='rainbow', legend='full')
        plt.title(f'tSNE on topic space using {self.cluster_method}');
        plt.figure(dpi=300)
        plt.hist(self.labels_, bins=self.n_clusters);
        plt.xlabel('Cluster')
        plt.ylabel('Number of Reviews in Cluster')
        plt.title('Reviews per Cluster')

    def kmeans(self, n_clusters):
        self.km = KMeans(n_clusters=n_clusters, random_state=42)
        self.labels_ = self.km.fit_predict(self.topic_data)
        self.cluster_method='kmeans'
        self.n_clusters=n_clusters
        self.cluster_centers=self.km.cluster_centers_

    def db(self, eps, min_samples):
        self.db = DBSCAN(eps=eps, min_samples=min_samples).fit(self.topic_data)
        core_samples_mask = np.zeros_like(self.db.labels_, dtype=bool)
        core_samples_mask[self.db.core_sample_indices_] = True
        self.labels_ = self.db.labels_
        self.cluster_method='db'
        n_clusters_ = len(set(self.labels_)) - (1 if -1 in self.labels_ else 0)
        self.n_clusters=n_clusters_

    def spectral(self, n_clusters):
        self.sc = SpectralClustering(n_clusters=n_clusters)
        self.labels_ = self.sc.fit_predict(self.topic_data)
        self.cluster_method='spectral'
        self.n_clusters=n_clusters

    def meanshift(self, quantile, n_samples):
        bandwidth = estimate_bandwidth(self.topic_data, quantile=quantile, n_samples=n_samples)
        self.ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
        self.ms.fit(self.topic_data)
        self.labels_ = self.ms.labels_
        self.cluster_method = 'meanshift'
        self.cluster_centers = self.ms.cluster_centers_

        labels_unique = np.unique(self.labels_)
        self.n_clusters = len(labels_unique)

        print("number of estimated clusters : %d" % self.n_clusters)


def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / np.sqrt(np.dot(vec1, vec1) * np.dot(vec2, vec2))


def best_cluster_ms(cluster, data, column):
    overall_clusters=[]
    for number in set(cluster.labels_):
        cluster_center = cluster.ms.cluster_centers_[number]
        distances=[]
        for index, vector in enumerate(cluster.topic_data):
            dist = cosine_similarity(cluster_center,vector)
            distances.append((dist, index))
        distances.sort()
        indices=[x[1] for x in distances[-4:]]
        print( f"\n + {distances[-4:]}")
        for i in indices:
            print("\n" + data[column].iloc[i])


def best_cluster(cluster, data, column):
    overall_clusters=[]
    for number in set(cluster.labels_):
        cluster_center = cluster.km.cluster_centers_[number]
        distances=[]
        for index, vector in enumerate(cluster.topic_data):
            dist = cosine_similarity(cluster_center,vector)
            distances.append((dist, index))
        distances.sort()
        indices=[x[1] for x in distances[-4:]]
        print( f"\n + {distances[-4:]}")
        for i in indices:
            print("\n" + data[column].iloc[i])


def making_vectorizers(data, components):
    count_vectorizer = CountVectorizer(ngram_range=(1, 2),
                                   stop_words='english',
                                   token_pattern="\\b[a-z][a-z]+\\b",
                                   lowercase=True,
                                   max_df = 0.6)
    tfidf_vectorizer =TfidfVectorizer(ngram_range=(1, 2),
                                   stop_words='english',
                                   token_pattern="\\b[a-z][a-z]+\\b",
                                   lowercase=True,
                                   max_df = 0.6)
    one=clustering_pipeline(count_vectorizer, n_components = components, reducer = TruncatedSVD)
    one.fit(data)
    two=clustering_pipeline(tfidf_vectorizer, n_components = components, reducer = TruncatedSVD)
    two.fit(data)
    return (one, two)


def many_kmeans(cluster, n_clusters, data, column):
    for i in range(1, n_clusters+1):
        cluster.kmeans(i)
        best_cluster(cluster, data, column)
        print('\n'+'-------------------------------------NEXT CLUSTER -------------------------------------------')


def many_db(cluster, eps, min_samples):
    cluster.db(eps, min_samples)


def many_spectral(cluster, n_clusters):
    for i in range(1, n_clusters+1):
        cluster.spectral(i)


def many_meanshift(cluster, quantile, n_samples, data, column):
    for i in range(4, n_samples+4):
        cluster.meanshift(quantile, i)
        best_cluster_ms(cluster, data, column)
        print('\n'+'-------------------------------------NEXT CLUSTER -------------------------------------------')
