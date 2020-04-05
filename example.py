# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 19:14:59 2019

@author: MabuXayda
"""

def tinh_tiendien(sudung):
    tien = 0
    if sudung > 400:
        tien += (sudung - 400) * 2927
        sudung = 400
    if sudung > 300:
        tien += (sudung - 300) * 2834
        sudung = 300
    if sudung > 200:
        tien += (sudung - 200) * 2536
        sudung = 200
    if sudung > 100:
        tien += (sudung - 100) * 2014
        sudung = 100
    if sudung > 50:
        tien += (sudung - 50) * 1734
        sudung = 50
    if sudung > 0:
        tien += sudung * 1678
    return tien

dien = []
tien = []

for i in range(0, 700, 20):
    dien.append(i)
    tien.append(tinh_tiendien(i))

from matplotlib import pyplot as plt
plt.figure()
plt.plot(dien, tien, marker='o', markersize=0)
plt.savefig("F:/temp/NordicCoder/python_analysis/dien.png", dpi=300)


n = 15
def print_item(n):
    l1 = list(map(str, range(1, n + 1)))
    l2 = ["".join(reversed(item)) for item in l1[1:]]
    l2.reverse()
    for i in range(n):
        print("".join(str(so) for so in l2+l1))
        rep = " " * len(l1[i])
        l1[i] = rep
        if i != 0:
            l2[-i] = rep
print_item(9)


import requests
import pandas as pd
from bs4 import BeautifulSoup
#=================================

url='http://www.vsd.vn/ModuleLichHoatDong/ThucHienQuyen/ThucHienQuyenSearch/?p_Search=&p_StockType=&p_Market=&p_StartDate=&p_EndDate=&_=1582182408260'
r = requests.get(url, verify=False);
content = r.content
soup = BeautifulSoup(content, "html.parser")
soup.prettify()
table = soup.find("table", {"class":"_tablelist"})
temp0 = table.find("tbody")
temp1 = temp0.findAll("tr")

hnx = pd.DataFrame(columns=['No', 'DATE', 'StockID', 'ISIN', 'Contents', 'StockType', 'Market', 'Location'])
for i in temp1:
    tds = i.findAll("td")
    hnx = hnx.append({
        'No':str(tds[0].string).strip(), \
        'DATE':str(tds[1].string).strip(), \
        'StockID':str(tds[2].string).strip(), \
        'ISIN':str(tds[3].string).strip(), \
        'Contents':str(tds[4].find("a").string).strip(), \
        'StockType':str(tds[5].string).strip(), \
        'Market':str(tds[6].string).strip(), \
        'Location':str(tds[7].find("span").string.strip())
        }, ignore_index=True)
