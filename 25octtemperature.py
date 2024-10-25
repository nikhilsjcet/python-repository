'''
Author: Nikhil Saju
Date:25/10/2024
Description:Python program to convert temperature values back and forth between Celsius and Fahrenheit. T
he user should be able to input a temperature in Celsius or Fahrenheit, and the program should convert it to the other unit using the formula:

'''

temperature= int(input("Enter the temperature"))
scale=input("Is this in (C)elsius or (F)ahrenheit ?")
if scale=="C":
   print("The temperature in fahrenheit is:",(9/5*temperature)+32)
else:
  print("The temperature in Celsius is:",(5/9*(temperature-32)))
