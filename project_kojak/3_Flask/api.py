import numpy as np
import pickle
import pandas as pd

from sklearn.decomposition import PCA
from sklearn.cluster import KMeans


df_std= pickle.load(open('./model/scaled_data.pkl', 'rb'))
names = pickle.load(open('./model/names.pkl', 'rb'))

pca_flask = PCA(n_components=100)
data_flask=pca_flask.fit_transform(df_std)
km_flask = KMeans(n_clusters=10, random_state=42)
labels_flask = km_flask.fit_predict(data_flask)

def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / np.sqrt(np.dot(vec1, vec1) * np.dot(vec2, vec2))

def prediction(user_input):
    output=[]
    user_input= list(names).index(user_input)
    overall_clusters=[]
    distances=[]
    for index, vector in enumerate(data_flask):
        dist = cosine_similarity(data_flask[user_input],vector)
        distances.append((dist, index))
    distances.sort()
    indices=[x[1] for x in distances[-4:]]
    for i in indices:
        output.append(names[i])
    results=[]
    for i in range(len(output[:3])):
        results.append(str(i+1) + ". " + output[:3][i]+ " ")
    a= output[:3]
    return results

if __name__ == '__main__':
    example = "Wellesley College"
    print(prediction(example))
