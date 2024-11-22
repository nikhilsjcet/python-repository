'''


Author:Nikhil Saju
Date:22/11/24
Program to Draw different type of triangles

'''



row=int(input("Enter the number of rows:"))
#Increasing Triangle
print("Increasing Triangle")
for i in range(0,row):
    for j in range(0,i+1):
        print("*",end="")
    print('')

#Decreasing Triangle
print("Decreasing Triangle")
row=int(input("Enter the number of rows:"))
for i in range(row,0,-1):
    for j in range(0,i):
        print("*",end="")
    print('')

#Hill Pattern
print("Hill Pattern")
row=int(input("Enter the number of rows:"))
for i in range(1,row+1):
    for j in range(row-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print('')

#Reverse Hill Pattern
print("Reverse Hill pattern")
row=int(input("Enter the number of rows:"))
for i in range(row,0,-1):
    for j in range(row-i,0,-1):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print('')