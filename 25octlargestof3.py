'''

Author : Nikhil Saju
Date: 25-10-2024
Description: Python program to find the largest of three numbers.
 The program should take three numbers as input from the user and determine which one is the largest.
 Use conditional statements to compare the numbers.
'''

numb1= int(input("Enter the first number"))
numb2= int(input("Enter the second number"))
if(numb1>numb2):
     print(numb1,"is greater than ",numb2)
     print("with in if")
else:
    print(numb2,"is greater than ",numb1)