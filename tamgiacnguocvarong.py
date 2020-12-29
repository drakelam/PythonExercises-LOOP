# Tam giác cân ngược
dinhdeptrai = int(5)

for i in range(dinhdeptrai,0,-1):
    for j in range(dinhdeptrai-i):
        print(' ', end="") # In ra khoảng trắng cách dấu *

    for j in range(2*i-1):
        print('*', end="")
    print() # in dòng mới



# Vừa rỗng vừa ngược
dinhdeptrai = int(5)

for i in range(1,dinhdeptrai+1) :

        # In ra khoảng trắng
        for j in range(1,i) :
            print (" ",end="")

        # Code tam giác vừa ngược vừa rỗng
        for j in range(1,(dinhdeptrai * 2 - (2 * i - 1)) +1) :
            if (i == 1 or j == 1 or j == (dinhdeptrai * 2 - (2 * i - 1))): # ##dinhdeptrai * 2 - (2 * i - 1)## # công thức
                print ("*", end="")
            else :
                print(" ", end="")
    print ("") # In ra dòng mới