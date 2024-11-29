'''
Author:Nikhil Saju
date:29/11/24
description:Program to check whether the given number is a valid mobile number or not using functions.

Rules:

    Every number should contain exactly 10 digits.
    The first digit should be 7 or 8 or 9

'''



def phn_num(num):
    count=len(num)
    if count==10:
       if num[0] in ["7","8","9"]:
        return True

num=input("Enter a phone number:")
if phn_num(num):
   print("It is a valid phone number")
else:
    print("It is a invalid phone number")