# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 16:30:49 2019

@author: MabuXayda
"""

"""============================================================================
1. Viết function truyền vào 2 số, in ra màn hình số lớn hơn
"""
def sosanh(a, b):
    if a == b:
        print("Hai so bang nhau")
    else:
        print(max(a, b))
sosanh(9, 9)

"""============================================================================
2. Viết function cho phép người dùng nhập vào 1 số tự nhiên, 
kiểm tra và xuất ra màn hình đó là số chẵn hay số lẻ
"""
def check_chia2():
    x = input("Moi nhap so: ")
    if int(x) % 2 == 0:
        print("So vua nhap la so chan")
    else:
        print("So vua nhap la so le")

check_chia2()

"""============================================================================
3. Viết function tryền vào 1 số, 
- trả về kết quả(True/False) là số có chia hết cho 3 hay không
"""
def check_chia3(x):
    if x % 3 != 0:
        return False
    return True

"""============================================================================
4. Viết function cho phép người dùng nhập vào 1 value(string) X bất kì, 
kiểm tra nếu 
X chia hết cho 3(dùng function ở câu 3) thì xuất ra giá trị của X/3.
Nếu X không chia hết cho 3 thì xuất ra giá trị của X bình phương
"""
def xuly_chia3():
    x = int(input("Moi nhap so: "))
    if check_chia3(x) :
        print(x/3)
    else:
        print(x**2)
    
xuly_chia3()

"""============================================================================
5. Viết function cho phép người dùng nhập vào 1 value(string) X bất kì. 
- In ra màn hình cho biết X đang viết hoa hay viết thường
- In ra màn hình X chỉ viết hoa chữ cái đầu
"""
def check_viethoa():
    x = input("Moi nhap text: ")
    if x.islower():
        print("Text viet thuong")
    elif x.isupper():
        print("Text viet hoa")
    print(x.capitalize())
    
check_viethoa()

"""============================================================================
6. Viết function truyền vào 2 String main_str và sub_str, 
- In ra màn hình kết quả sub_str có nằm trong main_str hay không.
- Nếu có thì trả về index đầu tiên của sub_str trong main_str
"""
def check_string(main, sub):
    if sub in main:
        print("Chuoi sub co nam trong chuoi main")
        print(main.find(sub))
    else:
        print("Chuoi sub khong nam trong chuoi main")

check_string("This is a master piece", "si")
    
    
            
