'''
Author : Nikhil saju
Date:8/11/2024
Description:Code to find the greatest and smallest of given n numbers
'''


n=int(input("Enter the list of numbers"))
n1=int(input("Enter the first number:"))
smallest=n1
largest=n1
while n>1:
    num=int(input("Enter next number:"))
    if num>largest:
         largest=num
    if num<smallest:
        smallest=num
    n-=1
print("Greatest number is",largest)
print("Smallest number is",smallest)



