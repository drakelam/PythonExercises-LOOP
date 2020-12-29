# Bài số 1 và 2 về vòng lặp while
# Bài số 1
#in ra tu 1 toi 100
i = 1
while (i <= 100):
    print(i)
    i+=1
# tiep theo chia het cho 3
# bat dau tu 20-50
print("In ra man hinh cac so tu chia het cho 3 tu 20-50 là: " )
i = 20
while i < 50:
      if i % 3 == 0:
            print(i)
      i += 1
##  Bài số 2
# Nhập số nguyên n
n=int(input("Nhập n="))
#  In ra tổng của các số từ 1 đến số vừa nhập vào bàn phím
i=1
while i <= n:
    print(i)
    i +=1

print("Em chào cả nhà ạ!")
# In ra cac so le tu 100-50
print("In ra màn hình các số lẻ đếm ngược từ 100-50 là: " )
i = 100
while i > 50:
      if i % 3 == 0:
            print(i)
      i -= 1
##
#
# Bài tập về vòng lặp For
#
##
# Bài số 1
# tính tổng và tổng bình phương của một trăm số nguyên đầu tiên
a=0
print("Tinh tong va tong binh phuong cua 1 tram so nguyen dau tien: ")
for i in range (1,101):
    a += i
    # tính tổng của một trăm số nguyên đầu tiên

print(a,a*a)
# Bài Số 2 - Tính Trung Bình cộng
n = int(input())
a=0
print("Tinh trung binh cong cua 1 tram so nguyen dau tien: ")
for i in range (1,n+1):
    a += i
    # tính tổng của một trăm số nguyên đầu tiên

print(a/100)
#
#
#Bài Số 3. Tìm giai thừa của 1 ố nhập từ bàn phím
print("Nhập giá trị n:")
n=int(input())
if n > 0:
    gt=1
    for i in range(1,n+1):
        gt=gt*i
    print("Giai thừa của", n, "bằng:",gt)
else:
    print("Vui lòng nhập n > 0")

# Xong phần Bài tập For 1

#
#BT Lab Python For 2.pdf
# Chia hết cho 3
print (" in ra tổng của các số nguyên nằm trong khoảng từ 200-600 chia hết cho 3")
for i in range(200, 601):
    if (i % 3 == 0):
     print(i)
#Chia hết cho 5
print (" in ra tổng của các số nguyên nằm trong khoảng từ 200-600 chia hết cho 3")
for i in range(50, 100):
    if (i % 5 == 0):
     print(i)





