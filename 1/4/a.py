#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 g <g@ABCL>
#
# Distributed under terms of the MIT license.
from sklearn.cluster import hierarchical
from sklearn import datasets
from sklearn import preprocessing

from scipy.cluster.hierarchy import dendrogram

import matplotlib.pyplot as plt
import numpy as np


def plot_dendrogram(model, **kwargs):

    # Children of hierarchical clustering
    children = model.children_

    # Distances between each pair of children
    # Since we don't have this information, we can use a uniform one for plotting
    distance = np.arange(children.shape[0])

    # The number of observations contained in each cluster level
    no_of_observations = np.arange(2, children.shape[0] + 2)

    # Create linkage matrix and then plot the dendrogram
    linkage_matrix = np.column_stack([children, distance,
                                      no_of_observations]).astype(float)

    # Plot the corresponding dendrogram

    dendrogram(linkage_matrix, **kwargs)


# import some data to play with
iris = datasets.load_iris()
feat = iris.feature_names
X = iris.data[:, :2]  # we only take the first two features. We could
# avoid this ugly slicing by using a two-dim dataset
y = iris.target
y_name = ['Setosa', 'Versicolour', 'Virginica']

from sklearn.cluster import AgglomerativeClustering
clustering = AgglomerativeClustering(linkage="single", n_clusters=150)
clustering.fit(X)

# MinMax scale the data so that it fits nicely onto the 0.0->1.0 axes of the plot.
X_plot = preprocessing.MinMaxScaler().fit_transform(X)

colours = 'rbg'
plt.title('Hierarchical Clustering Dendrogram')
plot_dendrogram(clustering, labels=clustering.labels_)
plt.show()
# for i in range(X.shape[0]):
#     plt.text(
#         X_plot[i, 0],
#         X_plot[i, 1],
#         str(clustering.labels_[i]),
#         color=colours[y[i]],
#         fontdict={
#             'weight': 'bold',
#             'size': 9
#         })

# plt.xticks([])
# plt.yticks([])
# plt.axis('off')
# plt.show()
