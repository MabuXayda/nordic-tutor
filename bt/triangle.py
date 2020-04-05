# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 21:03:26 2020

@author: MabuXayda
"""

"""
 START MODULE Thuc_triangle
"""
import math

def loaitamgiac(a,b,c):
    d = [a,b,c]
    d.sort()
    
    if a == b == c:
        return 'tam giac deu'
    #elif a == b or a == c or b == c:
    elif any([a == b, a == c, b == c]):
        return 'tam giac can'
    elif d[0]**2 + d[1]**2 == d[2]**2:
        return 'tam giac vuong'
    else:
        return 'tam giac thuong'
    
    
def chuvitamgiac(a,b,c):
    chuvi = a+b+c
    return chuvi
    

def dientichtamgiac(a,b,c):
    #tinh nua chu vi
    p = chuvitamgiac(a,b,c) / 2
    
    #tinh dien tich bang cong thuc Heron
    dientich = math.sqrt(p*(p-a)*(p-b)*(p-c))
    return dientich
    
"""
 END MODULE Thuc_triangle
"""