#list comprehention - create a new list in simple and with oneliner code
# syntx - [operation for var in itertable object]
# if contion is optional


# list1=[1,2,3,4,5,6,7,8,9,10]

# # write a program to take any number and prints its table

# usernum=int(input('Enter any number to print table:'))

# table=[num*usernum for num in list1 if usernum>=0]

# print('Table of',usernum,'using existing list object')
# for var in table:
#     print(var)

# print('Table of ',usernum,'using range()')

# table1=[num1*usernum for num1 in range(1,11)]


# for i in table1:
#     print(i)

# nested list comprehention 
# work nested list elemts 

list2=[[1,2,4],[3,4,5],[9,8,10,1,2,11,12]]

# conver nested list into normal list 
# convert nested list to set

newlist2=[var1 for row1 in list2 for var1 in row1]

print('Origin nested list:',list2)

print('new normal list: ',newlist2)
print('Set created using nestedlist:',set(newlist2))

