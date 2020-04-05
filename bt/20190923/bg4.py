# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 19:17:26 2019

@author: MabuXayda
"""

"""
Google Play Store Apps

Cho data Google Play Store Apps(link: https://www.kaggle.com/lava18/google-play-store-apps)

- Câu hỏi: làm sao để 1 app đạt được rating cao trên google play store.
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

_path = "F:/temp/democlass NC/googleplaystore.csv"
df = pd.read_csv(_path)

plt.figure(figsize=(8, 10))
sns.boxplot(data=df, y="Category", x="Rating")
#plt.xticks(rotation=90)
plt.xlim(3, 5)
plt.title("Boxplot of Rating VS Category")


l = [1, 10, 6,6,7,7,1,8,2,2,2,2,2,2,99999, 7,8]

l_sort = np.sort(l)

import numpy as np

print(np.quantile(l, 0.25))
