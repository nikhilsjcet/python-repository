'''
AUTHOR:NIKHIL SAJU
DATE:6/12/24
DESCRIPTION:Program to define a module to find Fibonacci Numbers and import the module to another program.

'''






def fibonacci_num(num):
    lst=[]
    num1=0
    num2=1
    for i in range(num):
        lst.append(num1)
        num1,num2=num2,num1+num2
    return lst
