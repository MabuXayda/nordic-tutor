# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 10:48:37 2020

@author: MabuXayda
"""
#%% 1
"""============================================================================
1. Viết function truyền vào 2 số, in ra màn hình số lớn hơn 
"""
#------- Cach 1
def sosanh_2so(so1, so2):
    if so1 > so2:
        print(so1)
    elif so2 > so1:
        print(so2)

#------- Cach 2
def sosanh_2so(so1, so2):
    if so1 != so2:
        print(max(so1, so2))

sosanh_2so(9, 7)

#%% 2
"""============================================================================
2. Viết function cho phép người dùng nhập vào 1 số tự nhiên, 
kiểm tra và xuất ra màn hình đó là số chẵn hay số lẻ
"""
def check_chan_le():
    so = input("Moi nhap so: ")
    if so % 2 == 0:
        print("So vua nhap la so chan")
    else:
        print("So vua nhap la so le")

#%% 3
"""============================================================================
3. Viết function tryền vào 1 số, 
- trả về kết quả(True/False) là số có chia hết cho 3 hay không
"""
#------- Cach 1
def sochiahetcho3(a):
    if a % 3 == 0:
        return True
    else:
        return False

#------- Cach 2
def sochiahetcho3(a):
    if a % 3 == 0:
        return True
    return False

#------- Cach 3
def sochiahetcho3(a):
    return a % 3 == 0

#%% 4
"""============================================================================
4. Viết function cho phép người dùng nhập vào 1 value(string) X bất kì, 
kiểm tra nếu 
X chia hết cho 3(dùng function ở câu 3) thì xuất ra giá trị của X/3.
Nếu X không chia hết cho 3 thì xuất ra giá trị của X bình phương
"""
#------- Cach 1   
def check_input():
    x =input('Nhap so kiem tra chia het cho 3= ')
    if x.isdigit():
        print("===== DEBUG 1: {}".format(type(x)))
        x = int(x)
        a = sochiahetcho3(x)
        print("===== DEBUG 2: {}".format(type(x)))
        if (a == 'True'):
            return (x/3)
        else:
           return (x**2)
    else:
        print('Chi xu ly so tu nhien')

#------- Cach 2
def check_input():
    x =input('Nhap so kiem tra chia het cho 3: ')
    if x.isdigit():
        x = int(x)
        if sochiahetcho3(x):
            return (x/3)
        else:
            return (x**2)
    else:
        print('Chi xu ly so tu nhien')

#%% 5
"""============================================================================
5. Viết function cho phép người dùng nhập vào 1 value(string) X bất kì. 
- In ra màn hình cho biết X đang viết hoa hay viết thường
- In ra màn hình X chỉ viết hoa chữ cái đầu
"""
def kiem_tra_hoa_thuong():
    g = input('Hay nhap mot chuoi: ')
    if g.islower():
        print('viet thuong toan bo')
    elif g.isupper():
        print('viet hoa toan bo')
    else:
        print('co ca viet hoa va thuong')
    
    print('viet hoa chu cai dau moi tu: ' + g.title())
    print('viet hoa chu cai dau tien: ' + g.capitalize())
    
kiem_tra_hoa_thuong()

#%% 6
"""============================================================================
6. Viết function truyền vào 2 String main_str và sub_str, 
- In ra màn hình kết quả sub_str có nằm trong main_str hay không.
- Nếu có thì trả về index đầu tiên của sub_str trong main_str
"""

main_str = "Python for DA for class 20191230"
sub_str = "for"

def bt6(x, y):
    if y in x:
        print("sub_str co nam trong main_str")
        return x.find(y)
    else:
        print("sub_str khong co nam trong main_str")

a = bt6(y=sub_str, x=main_str)
