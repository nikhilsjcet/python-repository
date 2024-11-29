'''
author:Nikhil Saju
date:29/11/24
Description:A program that accepts the lengths of three sides of a triangle as inputs.
The program should output whether or not the triangle is a right triangle
(Recall from the Pythagorean Theorem that in a right triangle,
the square of one side equals the sum of the squares of the other two sides).
Implement using functions.
'''



def check_triangle():
    list=[]
    s1 = int(input("Enter the length of first side:"))
    s2 = int(input("Enter the length of second side:"))
    s3 = int(input("Enter the length of third side:"))
    list.append(s1)
    list.append(s2)
    list.append(s3)
    list.sort()
    if list[2]**2==list[0]**2+list[1]**2:
        print("It is a right triangle")
    else:
        print("It is not a right triangle")
check_triangle()


