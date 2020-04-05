# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 15:00:40 2019

@author: MabuXayda
"""

#%% 15
"""============================================================================
15. Viết function tính tần suất xuất hiện các từ(cách nhau bởi dấu cách " ") 
từ input. In ra màn hình kết quả sau khi đã sắp xếp theo bảng chữ cái.
VD Input: 
New to Python or choosing between Python 2 and Python 3? Read Python 2 or 
Python 3.
- Output: 2:2 , 3.:1 , 3?:1 , New:1 , Python:5 , Read:1 , and:1 , between:1 ,
 choosing:1 , or:2 , to:1
"""
wordlist = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."

#------- Cach 1
def tansuat(txt):
    if len(txt) > 0:
        #tao list chua tung tu
        list_txt = txt.split()
        list_txt.count("2")
        
        #tao set chua gia tri khong duplicate
        set_txt = set(list_txt)
        
        #tao dictionary chua tan suat cac tu
        dic_txt = {}
        for tu in set_txt:
            print("Key: {} | Value: {}".format(tu, list_txt.count(tu)))
            dic_txt[tu] = list_txt.count(tu)    
            
        #in ra dictionary duoc sap xep tang dan
        #cach xep thu tu 1
        for i in sorted(dic_txt): 
            print({i: dic_txt[i]})
        #cach xep thu tu 2
        list_kq = [(key,dic_txt[key]) for key in dic_txt]
        list_kq.sort()
        print (list_kq)
        
tansuat(wordlist)

#------- Cach 2
def bai15_method2(wordlist):
    wordsfreq = {}
    for w in wordlist.split():
        print("Add key {} | value cu {} | value moi {}".format(w, wordsfreq.get(w,0), wordsfreq.get(w,0)+1))
        key = w
        value_cu = wordsfreq.get(w, 0)
        value_moi = value_cu + 1
        wordsfreq[key] = value_moi
        
        wordsfreq[w] = wordsfreq.get(w,0) + 1
        
    for key in sorted(wordsfreq):
        print("{}:{}".format(key,wordsfreq[key]))

bai15_method2(wordlist)

#%% 16
"""============================================================================
16.Viết module triangle trong đó có các hàm:
- kiểm tra xem tam giác là tam giác cân, tam giác đều, tam giác vuông 
hay thường?
- tính chu vi tam giác
- tính diện tính tam giác.
input các hàm trên là chiều dài 3 cạnh tam giác.
"""
from tutorial.bt import triangle as tri

def tamgiac(x,y,z):
    if x+y <= z or x+z <= y or y+z <= x:
        print('Day khong phai la tam giac.')
    else:
        ltg = tri.loaitamgiac(x,y,z)
        cvtg = tri.chuvitamgiac(x,y,z)
        dttg = tri.dientichtamgiac(x,y,z)
        print('Day la {}.'.format(ltg))
        print('Chu vi tam giac = {}'.format(cvtg))
        print('Dien tich tam giac = {}'.format(dttg))
        
tamgiac(4,3,5)

#%% 17
"""============================================================================
17. Xây dựng function trả về ma trận đơn vị kích thước N*N
VD Input: N = 3
Ouput = [[1,0,0],[0,1,0],[0,0,1]]
"""
#------- Cach 1
def cach1_identity_matrix(n):
    m = []
    while len(m) < n: # hang
        print('='*40)    
        print('len(m) = {}'.format(len(m)))
        print(m)
        m.append([])
        print('len(m) appended = {}'.format(len(m)))
        print(m)
        while len(m[-1]) < n: # cot
            print('-'*40)
            print('len(m[-1]) = {}'.format(len(m[-1])))
            print(m)
            m[-1].append(0)
            print('len(m[-1]) appended = {}'.format(len(m[-1])))
            print(m)
    for i in range(n):
        m[i][i] = 1
    return m
cach1_identity_matrix(3)

#------- Cach 2
def build_matrix(n):
    matrix = []
    for i in range(n):
        # print("====== matrix before : {}".format(matrix))
        mtx = []
        for j in range(n):
            if i == j:
                mtx.append(1)
            else:
                mtx.append(0)
            # print("====== mtx | {}".format(mtx))
        matrix.append(mtx)   
        # print("====== matrix after: {}".format(matrix))
    return matrix
mt = build_matrix(10)

#%% 17.1
"""============================================================================
17.1 In ma trận ở bài 17 dưới dạng ma trận N*N.
VD Input: N = 3
Output:
1,0,0
0,1,0
0,0,1
"""
#------- Cach 1
for line in mt:
    for so in line[:-1]:
        print("{}, ".format(so), end="")
    print(line[-1])

#------- Cach 2
for l in mt:
    print(", ".join(map(str, l)))

#%% 18
"""============================================================================
18. Xây dựng module mymath.py gồm các function sau:
- xuất ra giá trị xuất hiện nhiều nhất trong 1 list số, trả về nhiều giá trị 
nếu có.(gọi ý dùng mode() trong statistics)
VD: Input:[1,2,5,7,3,7,7,5,8,5]
Output: 5, 7

- tính giai thừa 1 số nguyên.
- kiểm tra 1 số có phải là số nguyên tố hay không? 
(số nguyên tố là số chỉ chia hết cho 1 và chính nó.)
- kiểm tra 1 số có phải số chính phương hay không? 
(số chính phương là số có căn bậc 2 là số tự nhiên.)
Tạo 1 file main.py để gọi hàm từ module mymath
"""
"""============================================================================
19. In ra 10 file với cấu trúc file như sau: dòng đầu là id file(id = 1,2..10), 
tiếp theo là n dòng "Hello world!" với n = id.
vd file 1:
id 1
Hello world!
file 2:
id 2
Hello world!
Hello world!
file 3 :
id 3
Hello world!
Hello world!
Hello world!
"""

#%% 20
"""============================================================================
20.
Viết hàm nhận vào file transaction.txt với dòng đầu tiên là id của tài khoản, 
dòng thứ 2 là số tài khoản, dòng thứ 3 là số dư tài khoản, các dòng tiếp theo 
hiển thị nội dung giao dịch 
    + Với D,100 là nộp vào ngân hàng 100. 
    + Với W,100 là rút ra 100 từ tài khoản. 
Hàm trả về số dư cuối cùng của tài khoản
vd input:
Id1
Tk01
400
D,100
W,200
-> output: 300
"""
s = "E:/Study/python/nc_python_analysis/tutorial/transaction.txt"

#------- Cach 1
def check_account(path):
    file = open(path)
    id_tk = file.readline()
    so_tk = file.readline()
    so_du = int(file.readline())
    for line in file:
        arr = line.split(",")
        if arr[0] == "D":
            so_du += int(arr[1])
        elif arr[0] == "W":
            so_du -= int(arr[1])
    file.close()
    print("Tai khoan ID: {} | SoTK: {} | So du: {}".format(
        id_tk, so_tk, so_du))
    return so_du
            
#------- Cach 2
def soDuTK(s):
    f = open(s)
    f.readline() #skip id
    f.readline() #skip so TK
    sodu = int(f.readline())
    nop = 0;
    rut = 0;
    for l in f: #tinh so du
        data = l.split(",")
        if(data[0] == 'D'):
            nop += int(data[1])
        if(data[0] == 'W'):
            rut += int(data[1])
    f.close()
    sodu += nop
    sodu -= rut
    return sodu

#------- Cach 3
import os
def bai20(duongdan):
    t = open(duongdan, 'r')
    dong = 1
    for l in t:
        if dong == 3:
            sodu = int(l)
        elif l[0] == 'D':
            temp = l.split(',')
            sotien = int(temp[1])
            sodu = sodu + sotien
        elif l[0] == 'W':
            temp = l.split(',')
            sotien = int(temp[1])
            sodu = sodu - sotien
        dong += 1
    
    print('So du cuoi cung: {}'.format(sodu))

#%% 21
"""============================================================================
21.
File txt với nội dung file theo cú pháp sau: file gồm nhiều dòng, mỗi dòng 
tương ứng với tên học sinh và điểm số học sinh được cách nhau bởi dấu phẩy.  
Ví  dụ:
Nam,10
Anh,9

Viết hàm với input đầu vào là đường dẫn của file, hàm trả về danh sách các bạn 
được điểm cao nhất và điểm cao nhất
"""
s = "E:/Study/python/nc_python_analysis/tutorial/diem_hs.txt"

#------- Cach 1
def FindScoreMax(s):
    list_hs = []
    f = open(s)
    maximum = 0
    for l in f: #Find Max
        data = l.split(",")
        score = int(data[1])
        if(score > maximum):
            maximum = score
    print("Score Max: {}".format(maximum))    
    f.close()
    
    f = open(s)
    for l in f: #Print Name list
        data = l.split(",")
        score = int(data[1])
        if(score == maximum):
            list_hs.append(data[0])
            # print(l)
    f.close()
    return list_hs, maximum
ds, diem = FindScoreMax(s)

#------- Cach 2
def stud_check(students):
    f = open(students,"rt")
    stud = {}
    score = []
    res = []
    for n in f:
        lst = n.split(",")
        stud[lst[0]] = int(lst[1])
        score.append(int(lst[1]))
    f.close()
    
    for i in stud:
        if stud[i] == max(score):
            res.append(i)
    return res, max(score)
ds, diem = stud_check(s)

#%% 22
"""============================================================================
22.
Một Robot di chuyển trong mặt phẳng bắt đầu từ điểm đầu tiên. 
Robot có thể di chuyển theo hướng UP, DOWN, LEFT và RIGHT với những bước 
nhất định. Dấu di chuyển của robot được lấy từ file txt đầu vào, với 2 dòng 
đầu tiên thể hiện vị trí điểm đầu tiên, các dòng tiếp theo thể hiện quá trình 
di chuyển trong đó các con số phía sau hướng di chuyển chính là số bước đi 
VD: Input: 
X0 4 
Y0 3 
UP 5 
DOWN 3 
LEFT 3 
RIGHT 3 

Hãy viết hàm trả về khoảng cách từ vị trí hiện tại đến vị trí đầu tiên, 
sau khi robot đã di chuyển một quãng đường với input là tên file txt.
"""

#%% 23
"""===========================================================================
23. Tìm số nguyên dương N bé nhất sao cho N chia hết cho tất cả các số trong 
đoạn [1, 20]
"""
232792560
#------- Cach 1
def cach1_least_common_multiple(rng):
    n = 1
    for x in rng:
        for y in rng:
            if (n * y) % x == 0: 
                n *= y 
                break
    return n

doan = range(1, 21)
print(cach1_least_common_multiple(doan))

#------- Cach 2s
a = 0
k = 20

while a < 20:
    for i in range(1,21):
        if k % i == 0:
            a += 1
            if a == 20:
                print(k)
                break
        else:
            a = 0
            k += 20
            
#%% 24
"""============================================================================
24. Viết function kiểm tra chuỗi kí tự ng dùng nhập vào từ bàn phím, điều kiện
tương tự như bài 11. Bổ sung thêm chức năng nếu như không thỏa điều kiện thì
cho phép người dùng nhập lại, nhưng tối đa ng dùng chỉ được nhập 4 lần.
"""
#------- Cach 1
def kiemtrachuoi():
    chuoi = input("Nhập chuỗi: ")
    if len(chuoi) < 8:
        print("Không hợp lệ!")
        return False
    
    i = 0
    test1 = []
    test2 = []
    
    while i < len(chuoi):
        print("DEBUG | i={} | chuoi[i] = {}".format(i, chuoi[i]))
        if chuoi[i].isupper():
            test1.append(chuoi[i])
        if chuoi[i].isdigit():
            test2.append(chuoi[i])
        i += 1
        
    if len(test1) > 0 and len(test2) > 0:
        print("Hợp lệ!")
        return True
    else:
        print("Không hợp lệ!")
        return False

def kiemtrachuoi_nangcao():
    for i in range(4):
        if kiemtrachuoi() == True:
            break

kiemtrachuoi_nangcao()

#------- Cach 2
def bai24():
    for attempt in range(4):
        txt = input('Xin nhap mot chuoi ky tu: ')
        if (len(txt) >=8 and (not txt.islower()) and (any(char.isdigit() for char in txt))): #it nhat mot ky tu so
            print('Chuoi vua nhap hop le.')
            break
        else:
            if 3 - attempt == 0:
                print('Ban da nhap sai 4 lan, ban khong duoc nhap nua.')
            else:
                print('Chuoi vua nhap khong hop le. \n'
                      'Ban con ' + str(3 - attempt) + ' lan nhap lai.')
                
def bai24():
    count = 0
    while count < 4:
        new_account = input('Enter new password: ')
        if (len(new_account) >=8 and (not new_account.islower()) and (any(char.isdigit() for char in new_account))): #it nhat mot ky tu so
            print('Valid password.')
            break
        else:
            print('Invalid password. \nPlease try again')
            count += 1
    print("Max attempt")
    return
bai24()
    
"""============================================================================
25.
Viết function cho phép người dùng nhập ngày, tháng, năm từ bàn phím.
In ra màn hình kiểm tra ngày người dùng vừa nhập:
    + là ngày thứ mấy trong tuần
    + là ngày thứ bao nhiêu trong năm
    + tháng đó có bao nhiêu ngày
    + năm đó có phải là năm nhuận hay không
"""
import datetime

def nhap_input():
    info_ngay = int(input("Nhap ngay :"))
    info_thang = int(input("Nhap thang :"))
    info_nam = int(input("Nhap nam :"))
    ngay = datetime.datetime(info_nam, info_thang, info_ngay)
    print(ngay.strftime("%A"))
    print(ngay.strftime("%j"))
    print(so_ngay_cua_thang(ngay))
    return ngay

def check_leapyear(n):
    if (n % 4 == 0) and (n % 100 == 0):
        return True
    if n % 4 == 0 :
        return True
    return False

def so_ngay_cua_thang (date):
    thang = date.month
    nam = date.year
    list_thang = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    if check_leapyear(nam) and (thang == 2):
        return 29
    else:
        return list_thang[thang]