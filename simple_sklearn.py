# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 17:31:05 2019

@author: MabuXayda
"""

import graphviz
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn import tree

iris = load_iris()

# Khoi tao model
clf = tree.DecisionTreeClassifier()
# Train model
clf = clf.fit(iris.data, iris.target)
# Predict with model
result = clf.predict(iris.data)

plt.figure(figsize=(15, 10))
tree.plot_tree(clf.fit(iris.data, iris.target))

dot_data = tree.export_graphviz(clf, out_file=None)
graph = graphviz.Source(dot_data)
graph.render("iris")