# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 18:01:37 2019

@author: MabuXayda
"""

# importing the required module 
import matplotlib.pyplot as plt
import numpy as np
np.set_printoptions(precision=3)

# x axis values 
x = [1,2,3] 
# corresponding y axis values 
y = [2,4,1] 

# plotting the points  
plt.plot(x, y)

# naming the x axis 
plt.xlabel('x - axis') 
# naming the y axis 
plt.ylabel('y - axis')

# giving a title to my graph 
plt.title('My first graph!') 
  
# function to show the plot 
plt.show()

#%% SIMPLE LINE CHART
# line 1 points 
x1 = [1,2,3] 
y1 = [2,4,1] 
# plotting the line 1 points  
plt.plot(x1, y1, label = "line 1") 
  
# line 2 points 
x2 = [1,2,3] 
y2 = [4,1,3] 
# plotting the line 2 points  
plt.plot(x2, y2, label = "line 2") 
plt.plot(x1, y1, label = "line 1") 
  
# naming the x axis 
plt.xlabel('x - axis') 
# naming the y axis 
plt.ylabel('y - axis') 
# giving a title to my graph 
plt.title('Two lines on same graph!') 
  
# show a legend on the plot 
plt.legend() 
  
# function to show the plot 
plt.show() 

#%% LINE CHART WITH PARAM
# x axis values 
x = [1,2,3,4,5,6] 
# corresponding y axis values 
y = [2,4,1,5,2,6] 

# https://matplotlib.org/2.0.2/api/colors_api.html
# plotting the points  
plt.plot(x, y, color='green', linestyle='dashed', linewidth = 5, 
         marker='o', markerfacecolor='red', markersize=12)
  
# setting x and y axis range 
plt.xlim(1,8) 
plt.ylim(1,8) 
  
# naming the x axis 
plt.xlabel('x - axis') 
# naming the y axis 
plt.ylabel('y - axis') 
  
# giving a title to my graph 
plt.title('Some cool customizations!') 
  
# function to show the plot 
plt.show() 

#%% BAR CHART
# x-coordinates of left sides of bars  
left = [1, 2, 3, 4, 5] 
  
# heights of bars 
height = [10, 24, 36, 40, 5] 
  
# labels for bars 
tick_label = ['one', 'two', 'three', 'four', 'five'] 
  
# plotting a bar chart 
plt.bar(left, height, tick_label=tick_label, 
        width=0.5, color=['red', 'green']) 
  
# naming the x-axis 
plt.xlabel('x - axis') 
# naming the y-axis 
plt.ylabel('y - axis') 
# plot title 
plt.title('My bar chart!') 
  
# function to show the plot 
plt.show() 

#%% HISTOGRAM
# frequencies 
ages = [2,5,70,40,30,45,50,45,43,40,44, 
        60,7,13,57,18,90,77,32,21,20,40] 
  
# setting the ranges and no. of intervals 
rang = (0, 100) 
bins = 10  
  
# plotting a histogram 
plt.hist(ages, bins, rang, color = 'green', 
        histtype = 'bar', rwidth = 0.8) 
  
# x-axis label 
plt.xlabel('age') 
# frequency label 
plt.ylabel('No. of people') 
# plot title 
plt.title('My histogram') 
  
# function to show the plot 
plt.show()

#%% SCATTER CHART
# x-axis values 
x = [1,2,3,4,5,6,7,8,9,10]
# y-axis values 
y = [2,4,5,7,6,8,9,11,12,12] 
  
# plotting points as a scatter plot 
plt.scatter(x, y, label= "stars", color= "green",  
            marker= "*", s=30) 
  
# x-axis label 
plt.xlabel('x - axis') 
# frequency label 
plt.ylabel('y - axis') 
# plot title 
plt.title('My scatter plot!') 
# showing legend 
plt.legend()
  
# function to show the plot 
plt.show() 

#%% PIE CHART
# defining labels 
activities = ['eat', 'sleep', 'work', 'play'] 
  
# portion covered by each label 
slices = [3, 7, 8, 6] 
  
# color for each label 
colors = ['r', 'y', 'g', 'b'] 
  
# plotting the pie chart 
plt.pie(slices, labels = activities, colors=colors,  
        startangle=90, shadow = True, explode = (0, 0, 0.1, 0), 
        radius = 1.2, autopct = '%.1f%%') 

# plotting legend 
plt.legend(bbox_to_anchor=(1, 1), loc='upper left') 
# showing the plot 
plt.show() 

#%% LINE CHART ON ARRAY
# setting the x - coordinates 
np.pi
x = np.arange(0, 2*(np.pi), 0.1) 
# setting the corresponding y - coordinates 
y = np.sin(x)
  
# potting the points 
plt.plot(x, y)

# function to show the plot 
plt.show() 

#%% SUB PLOT
def create_plot(ptype): 
    # setting the x-axis vaues 
    x = np.arange(-10, 10, 0.01) 
      
    # setting the y-axis values 
    if ptype == 'linear': 
        y = x 
    elif ptype == 'quadratic': 
        y = x**2
    elif ptype == 'cubic': 
        y = x**3
    elif ptype == 'quartic': 
        y = x**4
    return(x, y) 

# setting a style to use 
plt.style.use('fivethirtyeight') 

# create a figure 
fig = plt.figure() 
  
# define subplots and their positions in figure 
plt1 = fig.add_subplot(221) 
plt2 = fig.add_subplot(222) 
plt3 = fig.add_subplot(223) 
plt4 = fig.add_subplot(224) 
  
# plotting points on each subplot 
x, y = create_plot('linear') 
plt1.plot(x, y, color ='r') 
plt1.set_title('$y_1 = x$') 
  
x, y = create_plot('quadratic') 
plt2.plot(x, y, color ='b') 
plt2.set_title('$y_2 = x^2$') 
  
x, y = create_plot('cubic') 
plt3.plot(x, y, color ='g') 
plt3.set_title('$y_3 = x^3$') 
  
x, y = create_plot('quartic') 
plt4.plot(x, y, color ='k') 
plt4.set_title('$y_4 = x^4$') 
  
# adjusting space between subplots 
fig.subplots_adjust(hspace=.5,wspace=0.5) 
  
# function to show the plot 
plt.show()

#%% PANDAS PLOT
"""
https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html
"""

import pandas as pd
df = pd.DataFrame(np.random.randn(1000, 4),
                  columns=list('ABCD'))
df = df.cumsum()
df.plot()


#======
df3 = pd.DataFrame(np.random.randn(1000, 2), columns=['B', 'C']).cumsum()
df3['A'] = pd.Series(list(range(len(df3))))
df3.plot(x='A', y='B')

"""
Plotting methods allow for a handful of plot styles other than the default
line plot. These methods can be provided as the "kind" keyword argument to
plot(), and include:

    "bar" or "barh" for bar plots
    "hist" for histogram
    "box" for boxplot
    "kde" or "density" for density plots
    "area" for area plots
    "scatter" for scatter plots
    "hexbin" for hexagonal bin plots
    "pie" for pie plots
"""

#===== bar
# plt.figure()
temp = df.iloc[5]
df.iloc[5].plot(kind='bar')
df.iloc[5].plot.bar()

df2 = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])
df2.plot.bar()
df2.plot.bar(stacked=True)
df2.plot.barh(stacked=True)

#==== histogram
df4 = pd.DataFrame({'a': np.random.randn(1000) + 1, 'b': np.random.randn(1000),
                    'c': np.random.randn(1000) - 1}, columns=['a', 'b', 'c'])

# plt.figure()
df4.plot.hist(alpha=0.5)
df4.plot.hist(stacked=True)

#%% SEABORN PLOT
"""
https://seaborn.pydata.org/tutorial.html
"""

import seaborn as sns
tips = sns.load_dataset("tips")

#===== boxplot
sns.boxplot(x=tips["total_bill"])

q25 = tips["total_bill"].quantile(.25)
q75 = tips["total_bill"].quantile(.75)
q50 = tips["total_bill"].quantile(.50)
d = q75-q25
q0 = max(min(tips["total_bill"]), q25 - d)
q99 = min(max(tips["total_bill"]), q75 + d)

sns.set_style("whitegrid")
sns.boxplot(x="day", y="total_bill", data=tips)
sns.boxplot(x="day", y="total_bill", hue="smoker", data=tips, palette="Set3")

plt.figure(figsize=(7, 5))
sns.boxplot(x="day", y="total_bill", hue="smoker", data=tips, palette="Set3")
plt.title("boxplot total_bill by smoker")
plt.legend(bbox_to_anchor=(1, 1), loc='upper left')

#===== distplot
sns.distplot(tips["total_bill"])
sns.distplot(tips["total_bill"], kde=False)
sns.distplot(tips["total_bill"], hist=False, rug=True)
sns.distplot(tips["total_bill"], rug=True)

sns.kdeplot(tips["total_bill"], shade=True)
sns.rugplot(tips["total_bill"])

#===== joinplot
sns.jointplot(data=tips, x="total_bill", y="tip")
sns.jointplot(data=tips, x="total_bill", y="tip", kind="kde")
sns.jointplot(data=tips, x="total_bill", y="tip", kind="hex")

#===== scatterplot
sns.scatterplot(x="total_bill", y="tip", data=tips)
sns.scatterplot(x="total_bill", y="tip", data=tips, hue="sex")
sns.scatterplot(x="total_bill", y="tip", data=tips, hue="sex", style="smoker")

#===== pairplot
sns.pairplot(tips, hue="sex")

#===== catplot
sns.catplot(x="day", y="total_bill", data=tips)
sns.catplot(x="day", y="total_bill", data=tips, kind="swarm")
sns.swarmplot(x="day", y="total_bill", data=tips)

sns.catplot(x="day", y="total_bill", data=tips, kind="swarm", hue="sex")

#===== split figure
fig = plt.figure()
plt1 = fig.add_subplot(121) 
plt2 = fig.add_subplot(122)
sns.distplot(tips["total_bill"], ax=plt1)
sns.distplot(tips["tip"], ax=plt2)
fig.suptitle("money distribution")

g = sns.FacetGrid(tips, row="day", height=1.7, aspect=4)
# g = sns.FacetGrid(tips, col="day", height=1.7)
g.map(sns.distplot, "total_bill", hist=False, rug=True)

#===== regplot, lmplot
sns.regplot(x="total_bill", y="tip", data=tips)
sns.lmplot(x="total_bill", y="tip", data=tips)
sns.lmplot(x="total_bill", y="tip", data=tips, hue="sex")
sns.lmplot(x="total_bill", y="tip", data=tips, hue="smoker")

tips["total_bill"].corr(tips["tip"])
