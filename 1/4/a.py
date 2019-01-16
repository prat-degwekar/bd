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

import matplotlib.pyplot as plt
import numpy as np

# import some data to play with
iris = datasets.load_iris()
feat = iris.feature_names
X = iris.data[:, :2]  # we only take the first two features. We could
# avoid this ugly slicing by using a two-dim dataset
y = iris.target
y_name = ['Setosa', 'Versicolour', 'Virginica']

from sklearn.cluster import AgglomerativeClustering
clustering = AgglomerativeClustering(linkage="ward", n_clusters=3)
clustering.fit(X)

# MinMax scale the data so that it fits nicely onto the 0.0->1.0 axes of the plot.
X_plot = preprocessing.MinMaxScaler().fit_transform(X)

colours = 'rbg'
for i in range(X.shape[0]):
    plt.text(
        X_plot[i, 0],
        X_plot[i, 1],
        str(clustering.labels_[i]),
        color=colours[y[i]],
        fontdict={
            'weight': 'bold',
            'size': 9
        })

plt.xticks([])
plt.yticks([])
plt.axis('off')
plt.show()
