def string_reverse(str1):
    rev_str=''
    index=len(str1)
    while index>0:
        rev_str += str1[index-1]
        index = index - 1
    return rev_str

str1=input("Enter a string:")
result=string_reverse(str1)
print("The reverse of the given string is",result)
