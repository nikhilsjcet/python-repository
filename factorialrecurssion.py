'''
Author:Nikhil Saju
Date:29/11/2024
Description: Program to find the factorial of a number using Recursion.
'''



def factorial(num):
    if num==0:
        return 1
    else:
        return(num*factorial(num-1))


num=int(input("Enter the number:"))
result=factorial(num)
print(f"Factorial of {num} is {result}")

