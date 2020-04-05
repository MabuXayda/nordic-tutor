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
"""
Với mỗi column, xử lý, fill na, in ra số liệu tổng quan của columns đó

Reviews - chuyển sang kiểu int
Size - chuyển sang kiểu số, chuẩn hóa về cùng đơn vị đo
Installs - chuyển sang kiểu int
Price - chuyển sang kiểu float
Content Rating - chuẩn hóa lại các giá trị phân biệt(bỏ 17+, 10+, ....)
Android Ver - chuẩn hóa về version, chỉ lấy 2 số đầu. VD: 4.0.3 -> 4.0
Last Updated - chuyển sang kiểu DateTime
UpdateDays - Tạo thêm column mới, số ngày từ Last Update update tính tới 2020-01-01

Chuẩn hóa header, bỏ dấu cách ở giữa text

"""

import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
#%% LOAD DATA
_path = "E:/Study/python/nc_python_analysis/googleplaystore.csv"
data = pd.read_csv(_path)
data.shape

data["Rating"].isnull().sum()

# --- check dup all column
dup = data[data.duplicated(keep=False)]
data = data.drop_duplicates(keep="first")

data["App"].unique()
data["App"].nunique()

data = data.sort_values(["App", "Reviews"])
dup = data[data.duplicated("App", keep=False)]
data = data.drop_duplicates("App", keep="last")

data = data[data["Rating"].isnull()==False]
# missing_data = data.isnull().any(axis=0).reset_index()
#%% XU LY COLUMN TYPE
data["Type"].value_counts()

data = data[data["Type"].isin(["Free", "Paid"])]

#%% XU LY COLUMN REVIEW
data["Reviews"].dtype
data["Reviews"].describe()

data["Reviews"] = data["Reviews"].astype(int, errors="ignore")
data["Reviews"] = pd.to_numeric(data["Reviews"], errors="coerce")

temp = data["Reviews"].describe()
q10 = data["Reviews"].quantile(0.1)

sns.boxplot(data["Reviews"])
plt.xlim(0, 150000)

#%% XU LY CATEGORY
data["Category"].value_counts()

#%% XU LY GENRES
data["Genres"].value_counts()

#%% XU LY COLUMN SIZE
data["Size"].dtype
data["Size"].value_counts()

#===== Cach 1
temp = data["Size"].str.extract("([\d\.]*)([\w ]*)", expand=True)
temp.columns = ["value", "type"]
temp["value"] = pd.to_numeric(temp["value"], errors="coerce")
temp.loc[temp["type"] == "M", "value"] = temp["value"] * 1024
data["Size"] = temp["value"]

sns.jointplot(data=data, x="Rating", y="Size", kind="kde")

sns.lmplot(x="Rating", y="Size", data=data)
plt.savefig(os.getcwd() + "/tutorial/bt/rating_size.png", dpi=100)
data["Size"].corr(data["Rating"])

plt.figure()
sns.lmplot(x="Rating", y="Size", data=data, hue="Type")
plt.savefig(os.getcwd() + "/tutorial/bt/rating_size_type.png", dpi=100)
data[data["Type"]=="Paid"]["Size"].corr(data[data["Type"]=="Paid"]["Rating"])


# =============================================================================
# #===== Cach 2
# def xuly_size(row):
#     size = row["Size"]
#     if size == "Varies with device":
#         size = ""
#     if "M" in size:
#         size = size.replace("M", "")
#         size = float(size)
#         size = size * 1024
#     elif "k" in size:
#         size = size.replace("k", "")
#         size = float(size)
#     row["Size"] = size
#     return row
# 
# data = data.apply(xuly_size, axis=1)
# data["Size"] = pd.to_numeric(data["Size"], errors="coerce")
# data["Size"].describe()
# =============================================================================


temp = data.groupby('Category')['Size'].transform('mean')

#%% XU LY COLUMN INSTALLS
data["Installs"].value_counts()

data["Installs"] = data["Installs"].str.replace("+", "")
data["Installs"] = data["Installs"].str.replace(",", "")
data["Installs"] = data["Installs"].astype(int)


#%% XU LY PRICE
data["Price"].value_counts()

data["Price"] = data["Price"].str.replace("$", "")
data["Price"] = data["Price"].astype(float)

#===== ANALYSIS
data["Price"].describe()
data[data["Type"] == "Paid"]["Price"].describe()

sns.boxplot(data[data["Type"] == "Paid"]["Price"])
plt.xlim(0, 15)

sns.lmplot(x="Price", y="Rating", data=data[data["Type"] == "Paid"])
plt.xlim(0, 15)

data["Type"].value_counts()

#%% XU LY CONTENT RATING
data["Content Rating"].value_counts()

data["Content Rating"] = data["Content Rating"].str.split(" ").str.get(0)


# ANALYSIS
data.groupby('Content Rating')['Rating'].plot(kind='hist')

data.groupby('Content Rating')['Rating'].mean().plot(kind='bar')
plt.ylim(4, 4.4)

bins = [1, 3.5, 4, 4.5, 5]
group_names = ["Bad", "Medium", "Good", "VeryGood"]
data["rating_bin"] = pd.cut(data["Rating"], bins, labels=group_names,
                                 include_lowest=True)
data["rating_bin"].value_counts()
temp = data.groupby("Content Rating")["rating_bin"].value_counts().unstack()
temp = temp.fillna(0)
temp = temp.div(temp.sum(axis=1), axis=0)

sns.heatmap(temp)
sns.heatmap(temp, cmap="YlGnBu", annot=True, fmt=".2f")

temp = data.groupby("Content Rating")["rating_bin"].value_counts().reset_index(name="count")
temp1 = data["Content Rating"].value_counts().reset_index(name="sum")
temp1.columns=["Content Rating", "sum"]
temp = pd.merge(temp, temp1, on="Content Rating", how="left")
temp["percent"] = temp["count"] / temp["sum"]

temp2 = pd.pivot_table(data=temp, values="percent", index="Content Rating",
                       columns="rating_bin")
temp2 = temp2.fillna(0)
temp2 = temp2[group_names]

# plt.figure(figsize=(7, 7))
sns.heatmap(temp2, cmap="YlGnBu", annot=True, fmt=".2f")
plt.yticks(rotation=0)
plt.tight_layout()

data.plot(x='Content Rating', y='Rating', kind='box')
data.groupby("Content Rating")["Rating"].plot(kind='box')
sns.boxplot(x='Content Rating', y='Rating', data=data)

flights = sns.load_dataset("flights")
flights = flights.pivot("month", "year", "passengers")
ax = sns.heatmap(flights)

#%% XU LY LAST UPDATE
data["Last Updated"] = pd.to_datetime(data["Last Updated"], format="%B %d, %Y",
                                      errors="coerce")

#%% XU LY ANDROID VER
data["Android Ver"].value_counts()
data["Android Ver"] = data["Android Ver"].replace("Varies with device", "")

temp = data["Android Ver"].str.split(" ").str.get(0)
temp1 = temp.str.split(".").str[0] + "." + temp.str.split(".").str[1]
data["Android Ver"] = temp1.str.replace("W", "")

#%% PRE PROCCESS
data = data[data["Rating"].isnull()==False]
data = data.sort_values(["Last Updated"])

data = data.drop_duplicates(keep="first")
data = data.drop_duplicates("App", keep="last")


#%% VISUALIZE RATING
data['Rating'].describe()

plot = sns.distplot(data["Rating"], bins=50)
plot.set_xlabel("Rating")
plot.set_ylabel("Frequency")
plt.title("Distribution of Rating", size=20)

sns.boxplot(data["Rating"])
q25 = data["Rating"].quantile(.25)
q75 = data["Rating"].quantile(.75)
d = q75-q25
q0 = max(min(data["Rating"]), q25 - d)
q99 = min(max(data["Rating"]), q75 + d)

# sns.set()

plt.figure(figsize=(5, 8))
# sns.boxplot(data=data, x="Category", y="Rating")
sns.boxplot(data=data, y="Category", x="Rating")
# plt.xticks(rotation=90)
plt.grid()
plt.title("Boxplot of Rating VS Category")


plt.figure(figsize=(15, 5))
sns.boxplot(data=data, x="Category", y="Rating", hue="Type",
            fliersize=0, palette="Set2")
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig(os.getcwd() + "/rating_cate_type.png", dpi=100)

#%% VISUALIZE GENRES
temp = data['Genres'].str.split(';', expand=True)
temp = pd.merge(data[["App", "Rating", "Content Rating"]], temp,
                left_index=True, right_index=True)
temp.loc[temp[0] == temp[1], 1] = None

temp1 = pd.melt(temp, id_vars="App", value_name="Genre", value_vars=[0, 1])
temp1 = pd.merge(temp1, data[["App", "Rating", "Type"]], on="App", how="left")
temp1 = temp1.dropna(subset=["Genre"])
temp1 = temp1.sort_values("Genre")

plt.figure(figsize=(16, 5))
sns.boxplot(data=temp1, x="Genre", y="Rating", hue="Type", fliersize=0)
plt.xticks(rotation=90)
plt.ylim(2, 5)
plt.tight_layout()
plt.savefig(os.getcwd() + "/tutorial/bt/rating_genre_typeg.png", dpi=100)


# temp = pd.melt(temp, id_vars=["App", "Content Rating"], value_name="Genre", value_vars=[0, 1])