# Tam giác cân ngược
dinhdeptrai = int(5)

for i in range(dinhdeptrai,0,-1):
    for j in range(dinhdeptrai-i):
        print(' ', end="") # In ra khoảng trắng cách dấu *

    for j in range(2*i-1):
        print('*', end="")
    print("") # in dòng mới



# Vừa rỗng vừa ngược
dinhdeptrai = int(5)

for i in range(1,dinhdeptrai+1) :

        # In ra khoảng trắng
        for j in range(1,i) :
            print (" ",end="") # Nếu bỏ khoảng trắng print ("",end="") Sẽ in ra tam giác vuông ngược

        # Code tam giác vừa ngược vừa rỗng
        for j in range(1,(dinhdeptrai * 2 - (2 * i - 1)) +1) :
            if (i == 1 or j == 1 or j == (dinhdeptrai * 2 - (2 * i - 1))): # ##dinhdeptrai * 2 - (2 * i - 1)## # công thức
                print ("*", end="")
            else :
                print(" ", end="")
         print ("") # In ra dòng mới
#
#
#
#
#
    
# Kết quả ta có được như sau:
"D:\Lap trinh Python\bai tap mot\venv\Scripts\python.exe" "D:/Lap trinh Python/bai tap mot/tamgiacnguocvarong.py"
*********
 *******
  *****
   ***
    *
*********
 *     *
  *   *
   * *
    *
  
# Nếu giá trị mặc định của print (" ",end="") được thay đổi thành print ("",end="") không in ra và tạo khoảng trắng thì nó sẽ ra Tam giác vuông ngược.
***********
*       *
*     *
*   *
* *
*


Process finished with exit code 0
