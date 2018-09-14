
# coding: utf-8


import pandas as pd
import numpy as np

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans, DBSCAN, SpectralClustering, MeanShift, estimate_bandwidth
from sklearn.manifold import TSNE

from sklearn.metrics.pairwise import cosine_similarity

import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use("seaborn")



class clustering_pipeline:
    def __init__(self, n_components, reducer=PCA):
        self.n_dim = n_components
        self.reducer = reducer(n_components)

    def fit(self, data):
        self.data=self.reducer.fit_transform(data)

    def pca_plot(self):
        cumulative = np.cumsum(self.reducer.explained_variance_ratio_)
        plt.plot(cumulative)
        plt.xlabel('Number of terms')
        plt.ylabel('Explained variance')

    def kmeans(self, n_clusters):
        self.km = KMeans(n_clusters=n_clusters, random_state=42)
        self.labels_ = self.km.fit_predict(self.data)
        self.cluster_method='kmeans'
        self.n_clusters=n_clusters
        self.cluster_centers=self.km.cluster_centers_

    def db(self, eps, min_samples):
        self.db = DBSCAN(eps=eps, min_samples=min_samples).fit(self.data)
        core_samples_mask = np.zeros_like(self.db.labels_, dtype=bool)
        core_samples_mask[self.db.core_sample_indices_] = True
        self.labels_ = self.db.labels_
        self.cluster_method='db'
        n_clusters_ = len(set(self.labels_)) - (1 if -1 in self.labels_ else 0)
        self.n_clusters=n_clusters_

    def spectral(self, n_clusters):
        self.sc = SpectralClustering(n_clusters=n_clusters)
        self.labels_ = self.sc.fit_predict(self.data)
        self.cluster_method='spectral'
        self.n_clusters=n_clusters

    def meanshift(self, quantile, n_samples):
        bandwidth = estimate_bandwidth(self.data, quantile=quantile, n_samples=n_samples)
        self.ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
        self.ms.fit(self.data)
        self.labels_ = self.ms.labels_
        self.cluster_method = 'meanshift'
        self.cluster_centers = self.ms.cluster_centers_

        labels_unique = np.unique(self.labels_)
        self.n_clusters = len(labels_unique)

        print("number of estimated clusters : %d" % self.n_clusters)
        
    def tsne(self, n_components, perplexity):
        tsne = TSNE(n_components = n_components, perplexity = perplexity, random_state=42)
        plt.figure(dpi=300)
        vector_tsne = tsne.fit_transform(self.data)
        sns.scatterplot(vector_tsne[:, 0], vector_tsne[:, 1],hue=self.labels_, alpha=0.5, size = 0.5,
                        palette='rainbow', legend='full')
        plt.title(f'tSNE on topic space using {self.cluster_method}');
        plt.figure(dpi=300)
        plt.hist(self.labels_, bins=self.n_clusters);
        plt.xlabel('Cluster')
        plt.ylabel('Number of Reviews in Cluster')
        plt.title('Reviews per Cluster')
        
        
def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / np.sqrt(np.dot(vec1, vec1) * np.dot(vec2, vec2))

def best_cluster_ms(cluster, data, column):
    overall_clusters=[]
    for number in set(cluster.labels_):
        cluster_center = cluster.ms.cluster_centers_[number]
        distances=[]
        for index, vector in enumerate(cluster.data):
            dist = cosine_similarity(cluster_center,vector)
            distances.append((dist, index))
        distances.sort()
        indices=[x[1] for x in distances[-4:]]
        print( f"\n + {distances[-4:]}")
        for i in indices:
            print("\n" + column[i])

# look at edges vs centroid
def best_cluster(cluster, data, column):
    overall_clusters=[]
    for number in set(cluster.labels_):
        cluster_center = cluster.km.cluster_centers_[number]
        distances=[]
        for index, vector in enumerate(cluster.data):
            dist = cosine_similarity(cluster_center,vector)
            distances.append((dist, index))
        distances.sort()
        indices_closest=[x[1] for x in distances[-4:]]
        indices_furthest=[x[1] for x in distances[:4]]
        print( f"\n + {distances[-4:]}")
        print(" ")
        print('Closest to Center')
        for i in indices_closest:
            print(column[i])
        print(" ")
        print('Farthest from Center')
        for i in indices_furthest:
            print(column[i])    


def many_kmeans(cluster, n_clusters, data, column, components, perplex):
    for i in range(1, n_clusters+1):
        cluster.kmeans(i)
        cluster.tsne(components, perplex)
#         best_cluster(cluster, data, column)
        print('\n'+'-------------------------------------NEXT CLUSTER -------------------------------------------')

def many_db(cluster, eps, min_samples):
    cluster.db(eps, min_samples)
    print('\n'+'-------------------------------------NEXT CLUSTER -------------------------------------------')

def many_spectral(cluster, n_clusters):
    for i in range(1, n_clusters+1):
        cluster.spectral(i)
        print('\n'+'-------------------------------------NEXT CLUSTER -------------------------------------------')
        
def many_meanshift(cluster, quantile, n_samples, data, column):
    for i in range(7, n_samples+7):
        cluster.meanshift(quantile, i)
#         cluster.tsne(components, perplex)
#         best_cluster_ms(cluster, data, column)
        print('\n'+'-------------------------------------NEXT CLUSTER -------------------------------------------')
        

                     