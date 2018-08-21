
# coding: utf-8

import pandas as pd
import numpy as np

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.decomposition import NMF, TruncatedSVD
from sklearn.cluster import KMeans, DBSCAN, SpectralClustering, MeanShift
from sklearn.manifold import TSNE

from sklearn.metrics.pairwise import cosine_similarity

import matplotlib.pyplot as plt

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
        plt.scatter(vector_tsne[:, 0], vector_tsne[:, 1],c=self.labels_, alpha=0.5)
        plt.title(f'tSNE on topic space using {self.cluster_method}');
        plt.figure(dpi=300)
        plt.hist(self.labels_, bins=self.n_clusters);
        
    def kmeans(self, n_clusters):
        self.km = KMeans(n_clusters=n_clusters)
        self.labels_ = self.km.fit_predict(self.topic_data)
        self.cluster_method='kmeans'
        self.n_clusters=n_clusters
        self.cluster_centers=self.km.cluster_centers_
        
    def db(self, eps, min_samples):
        self.db = DBSCAN(eps=eps, min_samples=min_samples).fit(self.x)
        core_samples_mask = np.zeros_like(self.db.labels_, dtype=bool)
        core_samples_mask[self.db.core_sample_indices_] = True
        self.labels_ = self.db.labels_
        self.cluster_method='db'
        n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
        self.n_clusters=n_clusters

    def spectral(self, article, num_to_return, n_clusters):
        self.sc = SpectralClustering(n_clusters=n_clusters)
        self.labels_ = self.sc.fit_predict(self.topic_data)
        self.cluster_method='spectral'
        self.n_clusters=n_clusters
        
    def meanshift(self, quantile, n_samples):
        bandwidth = estimate_bandwidth(self.x, quantile=quantile, n_samples=n_samples)
        self.ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
        self.ms.fit(self.topic_data)
        self.labels_ = self.ms.labels_
        self.cluster_method = 'meanshift'
        self.cluster_centers = self.ms.cluster_centers_

        labels_unique = np.unique(self.labels_)
        self.n_clusters_ = len(labels_unique)

        print("number of estimated clusters : %d" % n_clusters_)
        result_texts = [self.texts[i] for i in results[1][0]]
        return result_texts


def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / np.sqrt(np.dot(vec1, vec1) * np.dot(vec2, vec2))


def best_cluster(cluster):
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
            print("\n" + df.review.iloc[i])


def making_vectorizers(data):
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
    one=clustering_pipeline(count_vectorizer, n_components = 20, reducer = TruncatedSVD)
    one.fit(data)
    two=clustering_pipeline(tfidf_vectorizer, n_components = 20, reducer = TruncatedSVD)
    two.fit(data)
    return (one, two)


def many_kmeans(cluster, n_clusters):
    for i in range(n_clusters):
        cluster.kmeans(i)
        best_cluster(cluster)


def many_db(cluster, eps, min_samples):
    cluster.db(eps, min_samples)


def many_spectral(cluster, article, num_to_return, n_clusters):
    for i in range(n_clusters):
        cluster.spectral(article, num_to_return, i)


def many_meanshift(cluster, quantile, n_samples ):
    for i in range(n_samples):
        cluster.meanshift(quantile, i)
        best_cluster(cluster)

