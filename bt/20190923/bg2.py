# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 17:02:02 2019

@author: MabuXayda
"""

"""============================================================================
6.1 Viết function truyền vào số nguyên dương n. Trả về list bình phương của
các số từ 1->n.
VD: 
input: 4
output: [1, 4, 9, 16]
"""
def tim_dayso(n):
    lst = []
    for i in range(n):
        lst.append((i + 1)**2)
    return lst

#a = tim_dayso(5)

"""============================================================================
7. Viết function truyền vào 2 tham số m:số dân hiện tại và n:số năm
trả về dân số của 1 nước sau n năm, tì lệ tăng dân số là 1.8% hàng năm
"""
def tinh_sodan(m, n):
    for i in range(n):
        m += m * 1.8 / 100
    print("Dan sao sau {} năm là: {}".format(n, int(m)))
    return int(m)

#tinh_sodan(1000, 4)

"""============================================================================
8. Viết function cho người dùng nhập chỉ số điện mới và cũ từ bàn phím.
In ra màn hình chỉ số cũ, chỉ số mới, tiền trả định mức, 
tiền trả vượt định mức, tổng tiền phải trả. 

Định mức sử dụng điện cho mỗi hộ là: 50 KW với giá 230đ/KW
Nếu phần vượt định mức <= 50KW thì tính giá 480đ/KW
Nếu 50KW < phần vượt định mức < 100KW thì tính giá 700đ/KW 
Nếu phần vượt định mức >= 100KW thì tính giá 900đ/KW 
"""
def tinh_tiendien():
    socu = int(input("Nhap so dien cu: "))
    somoi = int(input("Nhap so dien moi: "))
    print("So dien cu: {}".format(socu))
    print("So dien moi: {}".format(somoi))

    socu = 2000
    somoi=2320
    
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
def kiemtra_hocluc():
    d_toan = int(input("Diem toan: "))
    d_ly = int(input("Diem ly: "))
    d_hoa = int(input("Diem hoa: "))
    d_anh = int(input("Diem anh: "))
    d = [d_toan, d_ly, d_hoa, d_anh]
    tb = sum(d)/len(d)

    if tb >= 80 and min(d) >= 65:
        print("Loai Gioi")
    elif tb >= 65 and min(d) >= 50:
        print("Loai Kha")
    elif tb >= 50 and min(d) >= 20:
        print("Loai Trung Binh")
    else:
        print("Loai Yeu")

#kiemtra_hocluc()

"""============================================================================
10. Viêt function truyền vào 2 số A, B < 2000, trả về danh sách chứa tất cả
các số chia hết cho 7 nhưng không chia hết cho 5, nằm trong đoạn từ A 
đến B(tính cả A và B)
"""
def check_chia75(a, b):
    kq = []
    if not a < b < 2000:
        print("Tham so truyen vao khong dung yeu cau")
        return
    for i in range(a, b + 1, 1):
        if i%7 == 0 and i%5 != 0:
            kq.append(i)
    return kq

print(check_chia75(5, 200))
"""============================================================================
11. Viết function in ra màn hình xem chuỗi kí tự nhập vào từ người dùng có hợp
lệ hay không. Chuỗi hợp lệ là chuỗi có chiều dài ít nhất 8 kí tự, chứa ít nhất
một chữ in hoa, chứa ít nhất một kí tự dạng số.
"""
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
        
#check_chuoihople()
    
"""============================================================================
12. Tạo danh sách các số nguyên dương nhỏ hơn 60000 có đặc điểm sau: số đó 
gồm n chữ số, tổng lũy thừa bậc n của các chữ số đó bằng chính số đó
VD: 
    153 là số có 3 chữ số, 
    và 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
"""
#for so in range(60000):
#    total = 0
#    so_str = str(so)
#    for i in so_str:
#        total += int(i) ** len(so_str)
#    if total == so:
#        print(so)

"""============================================================================    
13. Cho trước 2 dictionary, viết chương trình kết hợp 2 dictionary đó, đối với 
các item có cùng key thì cộng value lại với nhau.
VD
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
output: {'a': 400, 'b': 400, 'd': 400, 'c': 300}
"""
def combine_dict(dt_a, dt_b):
    dt_c = {}
    for k in set(dt_a).union(set(dt_b)):
        value = 0
        if k in dt_a:
            value += dt_a[k]
        if k in dt_b:
            value += dt_b[k]
        dt_c[k] = value
    return dt_c

#d1 = {'a': 100, 'b': 200, 'c':300}
#d2 = {'a': 300, 'b': 200, 'd':400}
#d3 = combine_dict(d1, d2)

"""============================================================================
14. Viết function truyền vào số nguyên dương n <= 30, trả về dictionary có độ 
dài = n sao cho mỗi cặp item có dạng (x:x*x).
VD: 
với n = 5
output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
"""
def get_dict(n):
    if not 0 < n <= 30:
        print("n khong thoa dieu kien")
        return
    else:
        dt = {}
        i = 1
#        for i in range(1, n+1):
        while i <= n:
            dt[i] = i * i
            i += i
        return dt

#get_dict(5)
