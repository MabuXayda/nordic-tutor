# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 15:00:40 2019

@author: MabuXayda
"""

"""============================================================================
15. Viết function tính tần suất xuất hiện các từ(cách nhau bởi dấu cách " ") 
từ input. In ra màn hình kết quả sau khi đã sắp xếp theo bảng chữ cái.
VD Input: 
New to Python or choosing between Python 2 and Python 3? Read Python 2 or 
Python 3.
- Output: 2:2 , 3.:1 , 3?:1 , New:1 , Python:5 , Read:1 , and:1 , between:1 ,
 choosing:1 , or:2 , to:1
"""
def count_word(t):
    ts = t.split(" ")
    for i in sorted(set(ts)):
        print("{} : {}".format(i, ts.count(i)))

t = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."
count_word(t)

"""============================================================================
16.Viết module triangle trong đó có các hàm:
- kiểm tra xem tam giác là tam giác cân, tam giác đều, tam giác vuông 
hay thường?
- tính chu vi tam giác
- tính diện tính tam giác.
input các hàm trên là chiều dài 3 cạnh tam giác.
"""
def check_tam_giac(a,b,c):
    d = sorted([a,b,c])
    a = d[0]
    b = d[1]
    c = d[2]
    if a + b < c:
        print('Day khong phai la tam giac. ')
    elif (a == b or b == c or c == a) and (c*c == b*b + a*a):
        print('Tam giac vuong can. ')
    elif a == b == c:
        print('Tam giac deu. ')
    elif a == b or b == c or c == a:
        print('Tam giac can. ')
    elif c*c == b*b + a*a:
        print('Tam giac vuong. ')
    else:
        print('Tam giac thuong. ')


"""============================================================================
17. Xây dựng function trả về ma trận đơn vị kích thước N*N
VD Input: N = 3
Ouput = [[1,0,0],[0,1,0],[0,0,1]]
"""
def build_matrix(n):
    matrix = []
    for i in range(n):
        mtx = []
        for j in range(n):
            if i == j:
                mtx.append(1)
            else:
                mtx.append(0)
        matrix.append(mtx)   
#    for i in matrix:
#        print(i)
    return matrix

m = build_matrix(3)
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

"""============================================================================
21.
File txt với nội dung file theo cú pháp sau: file gồm nhiều dòng, mỗi dòng 
tương ứng với tên học sinh và điểm số học Python được cách nhau bởi dấu phẩy.  
Ví  dụ:
Nam,10
Nữ,9

Viết hàm với input đầu vào là đường dẫn của file, hàm trả về danh sách các bạn 
được điểm cao nhất và điểm cao nhất
"""

path = "F:/temp/NordicCoder/python_analysis/tutorial/diem_python.txt"
bai_21(path)
f_txtScore(path)
bt21(path)
# CACH 1
def bai_21(filename):
    f = open(path,"r")
    students = []
    marks = []
    for line in f:
        students.append(line[:line.index(",")])
        marks.append(int(line[line.index(",")+1:]))
    f.close()
    print(students)
    print(marks)
    
    max_mark = max(marks)
    print ("co ", marks.count(max_mark)," ban co diem cao nhat")
    for i in range(marks.count(max_mark)):
        j = marks.index(max_mark)
        print(students[j],marks[j])
        students.pop(j)
        marks.pop(j)
        
# CACH 2
def f_txtScore(filepath):
#    filepath = "C:/Users/honguyen/Desktop/txtScore.txt"
    f = open(filepath)
    l = []
    z = []
    N = []
    S = []
    O = []
    line = 0
    for x in f:
        line += 1
        l.append(x)
    for i in range(0, line):
        Name = z.copy()
        N1 = z.copy()
        
        Name.append(l[i])
        N1 = Name[0].split(",")
        N.append(N1[0])
        S.append(N1[1])
    
    for i in range(0, line):
        if S[i] == max(S):
            O.append(N[i] + "," + S[i])
 
    print(O)

# CACH 3
def bt21(path):
    ds = {}
#    with open(input("vui long paste duong dan file:"),"r") as openobj:
    with open(path,"r") as openobj:
        for line in openobj:
            ds = dict([line.split(',')])
    print ("diem cao nhat la " + str(max(ds.values())))
    print ("cac ban diem cao nhat la " + str(ds.keys()))
bt21 ()

get_ds_diemcao(path)
def get_ds_diemcao(path):
    f = open(path)
    ds = {}
    max_diem = 0
    for line in f:
        arr = line.split(",")
        ten = arr[0]
        diem = int(arr[1])
        if ten not in ds:
            ds[ten] = diem
        else:
            if ds[ten] < diem:
                ds[ten] = diem
        if max_diem < diem:
            max_diem = diem
    f.close()
    for d in ds:
        if ds[d] == max_diem:
            print("Ban {} co diem {}".format(d, ds[d]))
            
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

"""===========================================================================
23. Tìm số nguyên dương N bé nhất sao cho N chia hết cho tất cả các số trong 
đoạn [1, 20]
"""
# CACH 1
def so_nguyen_to (x):
    for i in range(2,x,1):
        if x % i == 0:
            return False
    return True

phan_tu = []
num = []
for i in range (2,20,1):
    if so_nguyen_to(i):
        phan_tu.append(i)
        num.append(1)

for i in range (2,20,1):
    if not so_nguyen_to(i):
        kq = i
        this_num = []
        this_fre = []
        while kq > 1:
            for j in phan_tu:
                if kq%j == 0:
                    try: 
                        this_num.index(j)
                    except:                        
                        this_num.append(j)
                        this_fre.append(1)
                    else:
                        this_fre[this_num.index(j)] += 1
                    finally:
                        kq = kq / j
                        break
        print (i)
        print (this_num)
        print(this_fre)

        for k in this_num:
            if this_fre[this_num.index(k)]>num[phan_tu.index(k)]:
                num[phan_tu.index(k)] = this_fre[this_num.index(k)]
                
tich = 1
for i in phan_tu:
    tich = tich * (i ** num[phan_tu.index(i)])
print(tich)
for i in range(2,20,1):
    if tich % i > 0:
        print("FALSE")


# CACH 2   
smallest_num = 1
for i in range (1,21):
    if smallest_num % i > 0: # If the number is not divisible by i
        for k in range (1,21):
            if (smallest_num * k) % i == 0: 
                # Find the smallest number divisible by i    
                smallest_num = smallest_num * k
                print("K: {}".format(k) )
                print("smallest_num: {}".format(smallest_num) )
                break
print (smallest_num)

# CACH 3
a = 0
k = 20

while a < 20:
    for i in range(1,21):
        if k % i == 0:
            a += 1
            #print(str(a) + "A")
            if a == 20:
                print(k)
                break
        else:
            a = 0
            k += 20


"""============================================================================
24. Viết function kiểm tra chuỗi kí tự ng dùng nhập vào từ bàn phím, điều kiện
tương tự như bài 11. Bổ sung thêm chức năng nếu như không thỏa điều kiện thì
cho phép người dùng nhập lại, nhưng tối đa ng dùng chỉ được nhập 4 lần.
"""
# CACH 1
def F_CheckPassword():
        n = 1
        while n <= 4:
            password = input("Nhập Password cần kiểm tra:" )
            check = "Password không hợp lệ"  
            check1 = len(password) >= 8 # Check lenght >=8
            check2 = False # Check Upper Case
            check3 = False # Check Numberic
            for x in password:
                try:
                    x = int(x) # Able casting to Int
                    check3 = True
                except ValueError: # Not Able casting to Int --> Str
                    if x == x.upper():
                        check2 = True
            if check1 == True and check2 == True and check3 == True:
                check = "Password hợp lệ!"
                print(check)
                break
            else:
                print(check)
                n = n + 1
        else:
            print("Bạn đã nhập 4 lần!")

F_CheckPassword()

# CACH 2
def check_chuoihople():
    s = input("Moi nhap chuoi: ")
    hl_len = False
    hl_char = False
    hl_num = False
    if len(s) >= 8:
        hl_len = True
    for i in s:
        if i.isupper():
            hl_char = True
        if i.isdigit():
            hl_num = True
    if hl_len == True and hl_char == True and hl_num == True:
        print("Chuoi vua nhap hop le")
        return True
    else:
        print("Chuoi vua nhap khong hop le")
        return False

def nhap_pass():
    dem = 0
    while not check_chuoihople():
#    while not check_chuoihople():
        if dem == 3:
            break
        dem += 1

nhap_pass()

"""============================================================================
25.
Viết function cho phép người dùng nhập ngày, tháng, năm từ bàn phím.
In ra màn hình kiểm tra ngày người dùng vừa nhập:
    + là ngày thứ mấy trong tuần
    + là ngày thứ bao nhiêu trong năm
    + tháng đó có bao nhiêu ngày
    + năm đó có phải là năm nhuận hay không
"""

# CACH 1
import datetime

def nhap_input():
    info_ngay = int(input("Nhap ngay :"))
    info_thang = int(input("Nhap thang :"))
    info_nam = int(input("Nhap nam :"))
    ngay = datetime.datetime(info_nam, info_thang, info_ngay)
    
    return ngay

def check_day(date):
    return date.strftime("%a")

def check_leapyear(n):
    if (n % 400 == 0) and (n % 100 == 0):
        return True
    if n % 4 == 0 :
        return True
    return False

def so_ngay_cua_thang (thang, nam):
    list_thang = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    if check_leapyear(nam) and (thang == 2):
        return 29
    else:
        return list_thang[thang]

the_date = nhap_input()
print ("This is ", check_day(the_date))
print ("This is day in year ", the_date.strftime("%j"))
the_Mon = int(the_date.strftime("%m"))
the_Year = int(the_date.strftime("%Y"))

print ("This month has ", so_ngay_cua_thang(the_Mon,the_Year), " days")
print ("This year is leap year? ",int(the_date.strftime('%Y')) % 4 == 0)

from dateutil.relativedelta import relativedelta
d1 = datetime.datetime(2019, 10, 28)
d2 = d1 + relativedelta(months=1)
d2 = d2.replace(day=1) - relativedelta(days=1)
print(d2.days)

# CACH 2

def f_checkdatetime():
#    global tototdays
    from datetime import datetime
    dd = 28
    mm = 10
    yyyy = 2019
#    dd = int(input("Nhập ngày: "))
#    mm = int(input("Nhập tháng: "))
#    yyyy = int(input("Nhập năm: "))
    x = datetime(yyyy,mm,dd)
    # Return day of week
    print("Today is " + x.strftime("%A"))
    # Leap year
    year_check = "Không phải năm nhuận"
    if yyyy % 400 == 0 or (yyyy % 4 == 0 and yyyy % 100 != 0):
        year_check = "Năm nhuận"
    print(year_check)
    # Return days of month
    def f_daysmonth(year_check,mm):
        if year_check == "Năm nhuận" and mm == 2:
            days_month = 29
        elif year_check != "Năm nhuận" and mm == 2:
            days_month = 28
        elif mm == 7 or mm == 8 or (mm % 2 != 0 and mm < 7) or (mm % 2 == 0 and mm > 7) :
            days_month = 31
        else:
            days_month = 30    
        return days_month
    print("Days of month: " + str(f_daysmonth(year_check, mm)))
    # Day th in year   
    totaldays = 0
    for k in range(1,mm):
        totaldays += f_daysmonth(year_check,k)
    totaldays += int(x.strftime("%d"))
    print(totaldays)

f_checkdatetime()
