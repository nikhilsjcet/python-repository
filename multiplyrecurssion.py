'''
Author:Nikhil Saju
Date:29/11/24
Description:Recursive function to multiply two positive numbers
'''



def multiply(num1,num2):
    if num2==1:
        return num1
    else:
        return num1+multiply(num1,num2-1)


num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
if num1>0 and num2>0:
    result=multiply(num1,num2)
    print("The product of two numbers is:",result)
else:
    print("The  number you entered is not a positive number")