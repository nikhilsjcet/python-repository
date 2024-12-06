def gcd(num1,num2):
    if num1%num2==0:
        return num2
    else:
        return gcd(num2,num1%num2)
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
if num1>0 and num2>0:
    print(f"The greater common divisor is {gcd(num1,num2)}")
else:
    print("You have entered a negative number")