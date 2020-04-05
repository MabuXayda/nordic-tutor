# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 17:02:02 2019

@author: MabuXayda
"""

#%% 6.1
"""============================================================================
6.1 Viết function truyền vào số nguyên dương n. Trả về list bình phương của
các số từ 1->n.
VD: 
input: 4
output: [1, 4, 9, 16]
"""

#------- Cach 1
def squarelist(so):
    return [i * i for i in range(1, so+1)]

#------- Cach 2
def squarelist(so):
    kq = []
    for i in range(1, so+1):
        kq.append(i*i)
    return kq

#------- Cach 3
def list_binhphuong_cach1(n):
    rng = range(1,n+1,1)
    lst = []
    for i in rng:
        print("=" *20)
        print("do dai cua list hien tai: {}".format(len(lst)))
        lst.append(i**2)
        print("i = {} | i**2 = {}".format(i, i**2))
        print("do dai cua list sau khi append: {}".format(len(lst)))
    return lst

#------- Cach 4
def list_binhphuong_cach2(n):
    i = 1
    lst = []
    while i <= n:
        lst.append(i**2)
        i += 1
    return lst

#%% 7
"""============================================================================
7. Viết function truyền vào 2 tham số m:số dân hiện tại và n:số năm
trả về dân số của 1 nước sau n năm, tì lệ tăng dân số là 1.8% hàng năm
"""
#------- Cach 1
def danso(sodan,sonam):
    i = 1
    while i <= sonam:
        sodan_tang = sodan * 1.8 / 100
        sodan = sodan + sodan_tang
        i += 1
    return round(sodan)

#------- Cach 2
def population_grow (m,n):
    n = range (n)
    for x in n:
        m = m*1.018
    return m

#------- Cach 3
def calc_population(m,n):
    i=1
    while i <= n:
        m = m * 1.018
        i+=1
    return round(m, 2)

kq = population_grow(10000,10)
print(kq)

#%% 8
"""============================================================================
8. Viết function cho người dùng nhập chỉ số điện mới và cũ từ bàn phím.
In ra màn hình chỉ số cũ, chỉ số mới, tiền trả định mức, 
tiền trả vượt định mức, tổng tiền phải trả. 

Định mức sử dụng điện cho mỗi hộ là: 50 KW với giá 230đ/KW
Nếu phần vượt định mức <= 50KW thì tính giá 480đ/KW
Nếu 50KW < phần vượt định mức < 100KW thì tính giá 700đ/KW 
Nếu phần vượt định mức >= 100KW thì tính giá 900đ/KW 
"""
#------- Cach 1
def tiendien():
    socu = int(input("Nhap so dien cu: "))
    somoi = int(input("Nhap so dien moi: "))
    print("So dien cu: {}".format(socu))
    print("So dien moi: {}".format(somoi))

    sudung = somoi - socu
    in_dm = min(sudung, 50)
    out_dm = max(sudung, 50) - 50
    print("So dinh muc: {}".format(in_dm))
    print("So vuot dinh muc: {}".format(out_dm))
    
    in_money = in_dm * 230
    out_money = 0
    if out_dm >= 100:
        out_money += (out_dm - 99) * 900
        out_dm = 99
    if out_dm > 50:
        out_money += (out_dm - 50) * 700
        out_dm = 50
    if out_dm > 0:
        out_money += out_dm * 480
    print("Tien tra dinh muc: {}".format(in_money))
    print("Tien tra vuot dinh muc: {}".format(out_money))
    print("Tong tien phai tra: {}".format(in_money + out_money))

tinh_tiendien()

#------- Cach 2
def tiendien():
    while True:
        num = input('Xin nhap chi so dien cu: ')
        try:
            socu = int(num)
            break;
        except ValueError:
            try:
                socu = float(num)
                break;
            except ValueError:
                print ('Ban da nhap mot chuoi, khong phai so. \n'
                       'Vui long nhap lai so.')
    while True:
        num = input('Xin nhap chi so dien moi: ')
        try:
            somoi = int(num)
            break;
        except ValueError:
            try:
                somoi = float(num)
                break;
            except ValueError:
                print ('Ban da nhap mot chuoi, khong phai so. \n'
                       'Vui long nhap lai so.')
    d = somoi - socu
    tdm = 0
    tvdm = 0
    
    if d <= 50:
        prize = d * 230
        tdm = prize
    elif d <= 100:
        prize = (50 * 230) + (d -50)*480
    elif d <= 149:
        prize = (50 * 230) + (50 *480) + (d - 100)*700
    elif d > 149:
        prize = (50 * 230) + (50* 480) + (49 * 700) + (d - 149)*900
    
    if d > 50:
        tdm = 50 * 230
        tvdm = prize - tdm
    
    print('Chi so cu: ' + str(socu))
    print('Chi so moi: ' + str(somoi))
    print('Tien tra dinh muc: ' + str(tdm))
    print('Tien tra vuot dinh muc: ' + str(tvdm))
    print('So tien phai tra: ' + str(tdm+tvdm))
tiendien()

#------- Cach 3
def tiendien():
    oldIndex = int(input("Nhap so dien cu: "))
    newIndex = int(input("Nhap so dien moi: "))
    
    print("Chi so cu la: " + str(oldIndex))
    print("Chi so moi la: " + str(newIndex))
    if newIndex >= oldIndex:
        prize = 0
        consumePower = newIndex - oldIndex
        if consumePower <= 50:
            prize = consumePower * 230
        elif consumePower <= 100:
            prize = (50 * 230) + (consumePower -50)*480
        elif consumePower <= 149:
            prize = (50 * 230) + (50 *480) + (consumePower - 100)*700
        elif consumePower > 149:
            prize = (50 * 230) + (50* 480) + (49 * 700) + (consumePower - 149)*900
        
        print("Tien phai tra: "+ str(prize))

tiendien()

#%% 9
"""============================================================================
9. Viết function trả về kết quả xếp loại học lực của học sinh. 
Giả sử học sinh chỉ có bốn cột điểm Toán (T), Lý (L), Hóa (H) và Anh văn (AV). 
Điểm 4 môn được nhập vào từ bàn phím và theo thang điểm 100. 

Qui tắc xếp loại như sau:
    + Nếu trung bình 4 môn lớn hơn hoặc bằng 80 và không có môn nào nhỏ hơn 65, 
    thì xếp loại Giỏi.
    + Nếu học sinh không đủ điều kiện đạt loại giỏi, mà có trung bình 4 môn 
    lớn hơn hoặc bằng 65 và không có môn nào nhỏ hơn 50, thì xếp loại Khá.
    + Nếu học sinh không đủ điều kiện đạt loại Khá, mà có trung bình 4 môn 
    lớn hơn hoặc bằng 50 và không có môn nào nhỏ hơn 20, thì xếp loại 
    Trung bình.
    + Nếu học sinh không đạt 3 loại trên thì xếp loại Yếu.
"""
#------- Cach 1
def xeploai():
    while True:
        num = input('Xin nhap diem Toan: ')
        try:
            t = float(num)
            if 0 <= t <= 100:
                break
            print('Ban da nhap diem < 0 hoac > 100. \nVui long nhap lai diem.')
        except ValueError:
            print ('Ban da nhap mot chuoi, khong phai so. \nVui long nhap lai so.')
    
    
    
    while True:
        num = input('Xin nhap diem Ly: ')
        try:
            l = int(num)
            if 0 <= l <= 100:
                break
            print('Ban da nhap diem < 0 hoac > 100. \nVui long nhap lai diem.')
        except ValueError:
            try:
                l = float(num)
                if 0 <= l <= 100:
                    break
                print('Ban da nhap diem < 0 hoac > 100. \nVui long nhap lai diem.')
            except ValueError:
                print ('Ban da nhap mot chuoi, khong phai so. \nVui long nhap lai so.')
    while True:
        num = input('Xin nhap diem Hoa: ')
        try:
            h = int(num)
            if 0 <= h <= 100:
                break
            print('Ban da nhap diem < 0 hoac > 100. \nVui long nhap lai diem.')
        except ValueError:
            try:
                h = float(num)
                if 0 <= h <= 100:
                    break
                print('Ban da nhap diem < 0 hoac > 100. \nVui long nhap lai diem.')
            except ValueError:
                print ('Ban da nhap mot chuoi, khong phai so. \nVui long nhap lai so.')
    while True:
        num = input('Xin nhap diem Anh van: ')
        try:
            av = int(num)
            if 0 <= av <= 100:
                break
            print('Ban da nhap diem < 0 hoac > 100. \nVui long nhap lai diem.')
        except ValueError:
            try:
                av = float(num)
                if 0 <= av <= 100:
                    break
                print('Ban da nhap diem < 0 hoac > 100. \nVui long nhap lai diem.')
            except ValueError:
                print ('Ban da nhap mot chuoi, khong phai so. \nVui long nhap lai so.')
                
    if (t+l+h+av)/4 >= 80 and t>=65 and l>=65 and h>=65 and av>=65 :
        print('Hoc sinh gioi')
    elif (t+l+h+av)/4 >= 65 and t>=50 and l>=50 and h>=50 and av>=50 :
        print('Hoc sinh kha')
    elif (t+l+h+av)/4 >= 50 and t>=20 and l>=20 and h>=20 and av>=20 :
        print('Hoc sinh trung binh')
    else:
        print('Hoc sinh yeu')
                
xeploai()

#------- Cach 2
def xeploai():
    MAT = float(input("Please enter MATH score: "))
    PHY = float(input("Please enter PHYSICS score: "))
    CHE = float(input("Please enter CHEMISTRY score: "))
    ENG = float(input("Please enter ENGLISH score: "))
    score = [MAT,PHY,CHE,ENG]
    ave = round(sum(score)/len(score))
    if max(score) > 100 or min(score) < 0:
        return "Please re-enter score with 100 point scale!"        
    print(score)
    print(ave)
    if min(score) >= 65 and ave >= 80:
        return "Execellent! G"
    if min(score) >= 50 and ave >= 65:
        return "Good! K"
    if min(score) >= 20 and ave >= 50:
        return "Average! TB"
    return "Weak! Y"

rate = xeploai()

#%%10
"""============================================================================
10. Viêt function truyền vào 2 số A, B < 2000, trả về danh sách chứa tất cả
các số chia hết cho 7 nhưng không chia hết cho 5, nằm trong đoạn từ A 
đến B(tính cả A và B)
"""
#------- Cach 1
def taolist(a,b):
    c = []
    if (a <2000) and (b<2000):
        while a<=b:
            if (a % 7 == 0) and ( a % 5 != 0):
                c.append(a)
            a += 1
        else:
            print("Danh sách các số thỏa điều kiện: " + str(c))
    else:
        print ("2 số A,B < 2000 mới được")
    return c

#------- Cach 2
def taolist(a,b):
    list = []
    if a < 2000 and b < 2000:
        while a <= b:
            if a % 7 == 0 and a % 5 != 0:
                list.append(a)
            a += 1
        print(list)
    else:
        print("Chưa hợp lệ! Hai số không nhỏ hơn 2000")

#------- Cach 3
def taolist(a, b):
    if a < 2000 and b < 2000 and a <= b:
        kq = []
        for i in range(a, b+1):
            if i%7 == 0 and i%5 != 0:
                kq.append(i)
        print(kq)
    else:
        print("Input không thỏa")
        
kq = taolist(500, 50)

#%% 11
"""============================================================================
11. Viết function in ra màn hình xem chuỗi kí tự nhập vào từ người dùng có hợp
lệ hay không. Chuỗi hợp lệ là chuỗi có chiều dài ít nhất 8 kí tự, chứa ít nhất
một chữ in hoa, chứa ít nhất một kí tự dạng số.
"""
#------- Cach 1
def kiemtrachuoi():
    while True:
        txt = input('Xin nhap mot chuoi ky tu: ')
        if (len(txt) >=8 and (not txt.islower()) and (any(char.isdigit() for char in txt))): #it nhat mot ky tu so
            print('Chuoi vua nhap hop le.')
            break
        else:
            print('Chuoi vua nhap khong hop le. \nVui long nhap lai.')

#------- Cach 2
def kiemtrachuoi():
    chuoi = input("Nhập chuỗi: ")
    if len(chuoi) < 8:
        print("Không hợp lệ!")
        return None
    
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
    else:
        print("Không hợp lệ!")

kiemtrachuoi()

#%% 12
"""============================================================================
12. Tạo danh sách các số nguyên dương nhỏ hơn 60000 có đặc điểm sau: số đó 
gồm n chữ số, tổng lũy thừa bậc n của các chữ số đó bằng chính số đó
VD: 
    153 là số có 3 chữ số, 
    và 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
"""
#------- Cach 1
def kiemtraso(i): # Armstrong number, narcissistic number
    sodangxet = i-1 # nho hon so cho truoc
    lst_ketqua = []
    
    while sodangxet > 0: # so nguyen duong
        a = sodangxet
        n = int(len(str(a))) # so chu so, cung la bac luy thua
    
        cacchuso = []
        cacsoluythua = []
        
        while a > 0:
            chuso = a % 10
            a = int(a / 10)
            cacchuso.append(chuso)
            
        for so in cacchuso:
            soluythua = so**n
            cacsoluythua.append(soluythua)
    
        tongluythua = sum(cacsoluythua)
        if tongluythua == sodangxet:
            lst_ketqua.append(sodangxet)
        sodangxet -= 1
    
    # neu lst_ketqua khong co phan tu nao
    if not lst_ketqua:
        print('Khong co so nao thoa yeu cau.')
    else:
        print('Co ' + str(len(lst_ketqua)) + ' so thoa yeu cau.')
        return lst_ketqua

#------- Cach 2
def kiemtraso(i): # Armstrong number, narcissistic number
    sodangxet = i-1 # nho hon so cho truoc
    lst_ketqua = []
    while sodangxet > 0: # so nguyen duong
        n = int(len(str(sodangxet))) # so chu so, cung la bac luy thua    
        cacchuso = [int(c) for c in str(sodangxet)]
        tongluythua = 0 # neu khong khai bao se bi loi o vong lap duoi
        
        for so in cacchuso:
            tongluythua += so**n
        
        if tongluythua == sodangxet:
            lst_ketqua.append(sodangxet)
        sodangxet -= 1
    
    # neu lst_ketqua khong co phan tu nao
    if not lst_ketqua:
        print('Khong co so nao thoa yeu cau.')
    else:
        print('Co ' + str(len(lst_ketqua)) + ' so thoa yeu cau.')
        return lst_ketqua

#------- Cach 3
def kiemtraso():
    list_so = []
    for sodotim in range(1, 60000):
        i = 0
        pheptinh = 0
        while i < len(str(sodotim)):
            pheptinh += int(str(sodotim)[i]) ** len(str(sodotim))
            i +=1
        if sodotim == pheptinh:
            list_so.append(sodotim)
    print(len(list_so))
    return(list_so)

kiemtraso()

#------- Cach 4
lst = []
for so in range(1, 60000):
    total = 0
    so_str = str(so)
    for i in so_str:
        total += int(i) ** len(so_str)
        if total > so:
            break
    if total == so:
        lst.append(so)

#%% 13
"""============================================================================    
13. Cho trước 2 dictionary, viết chương trình kết hợp 2 dictionary đó, đối với 
các item có cùng key thì cộng value lại với nhau.
VD
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
output: {'a': 400, 'b': 400, 'd': 400, 'c': 300}
"""
#------- Cach 1
ini_dict = [{'a': 100, 'b': 200, 'c':300}, 
            {'a': 300, 'b': 200, 'd':400}]
  
# printing initial dictionary 
print ("initial dictionary", str(ini_dict)) 

# sum the values with same keys 
result = {} 
for d in ini_dict: 
    for k in d.keys(): 
        result[k] = result.get(k, 0) + d[k] 
print("resultant dictionary : ", str(result))

#------- Cach 2
def bai13_cach1(dic1,dic2):
    ketqua = dic1.copy()
    for x in dic2:
        if x in ketqua:
            ketqua[x] += dic2[x]
        else:
            ketqua[x] = dic2[x]
            
    return ketqua

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
z = bai13_cach1(d1,d2)

#------- Cach 3
def bai13_cach2(dic1,dic2):
    from collections import Counter
    ketqua = Counter(dic1) + Counter(dic2)
    return ketqua

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
z = bai13_cach2(d1,d2)

#------- Cach 4
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d3 = {}
d3.update(dict.fromkeys(d1))
d3.update(dict.fromkeys(d2))
for x in d3:
    d3[x]= d1.get(x,0) + d2.get(x,0)

#%% 14
"""============================================================================
14. Viết function truyền vào số nguyên dương n <= 30, trả về dictionary có độ 
dài = n sao cho mỗi cặp item có dạng (x:x*x).
VD: 
với n = 5
output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
"""
#------- Cach 1
def bai14(x):
    d = dict()
    if 0 < x <= 30:
        for i in range(1, x+1):
            d[i] = i*i
        print(d)
        return d
    else:
        return "This number is more than 30."
kq = bai14(8)

#------- Cach 2
def bai14(n):
    if 0 < n <= 30:
        dic = {}
        while n > 0:
            dic[n] = n*n
            n -= 1
        return dic
    else:
        print('So nhap vao phai > 0 va <= 30')
    
kq = bai14(8)


#------- Cach 3
def bai_14(n):
    if n <= 0 or n > 30:
        return ("So truyen vao khong dung!!!")
    ketqua = {}
    for i in range(1,n+1):
        ketqua[i] = i*i
    return ketqua

kq = bai_14(8)

