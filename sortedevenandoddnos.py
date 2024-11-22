'''
Author:Nikhil Saju
date:22/11/24 Program to sort even numbers first and odd numbers second'''
list1=[1,2,3,4,5,6,7]
list2=[8,9,10,11,12,13]
combined_list=list1+list2
even_list=[]
odd_list=[]
for i in combined_list:
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)
even_list.sort()
odd_list.sort()
merged_list=even_list+odd_list
print("The First list:",list1)
print("The Second list:",list2)
print("The Merged list:",merged_list)