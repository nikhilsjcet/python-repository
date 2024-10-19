'''
Author: Nikhil Saju
Date: 19-18-2024
Description:program that performs the following tasks:
    Create two separate strings:
        The first string should contain your first name.
        The second string should contain your last name.
    Concatenate the two strings with a space in between
    and store the result in a new variable.
    Print the concatenated string.
    From the concatenated string:
        Access and print a sub-string that consists of the last name only.
        Use string slicing to extract the sub-string.
Enter your first name:NIkhil
Enter your last name:Saju
NIkhil Saju
5
 Saju
 NIkhil



'''

first_name = input("Enter your first name")
last_name =  input("Enter your last name")
name= first_name+" " + last_name
print(name)
first_name_length=len(first_name)
print(first_name_length)
extracted_last_name=name[first_name_length +1:]
print(extracted_last_name)