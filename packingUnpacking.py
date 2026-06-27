#Packing  with list 
a=100
b='abc'
c=123
d='hello'
num=a,b,c,d

l=[a,b,c,d]
print('list elements after packing using direct assignment -',l)

#Using type casting, first create tuple and then convert it to list
num=a,b,c,d
l1=list(num)
print('list elements after packing using typecasting -',l1)


#Unpacking list 
#varibale count should be equal to list size(no of elements)
list3=['abc',100,25,6,7]

p,q,r,s,t=list3

print('Each element after unpacking')
print('Element 1=',p)
print('Element 2=',q)
print('Element 3=',r)
print('Element 4=',t)

list3.append(100)
list3.extend(l1)

#unapcking using * operator 
#We can use * operator to unpack the remaining elements of a list into a variable. 

x,y,*z=list3 # * using at last 

print('Each element after unpacking using * operator at last ')
print('Element 1=',x)
print('Element 2=',y)
print('Remaining items-',z)

l,*m,n=list3 # * using at middle 

print('Each element after unpacking using * operator at last ')
print('Element 1=',l)
print('middle elemets=',m)
print('Last element-',n)


#Unapck nested list 

list4=[0,[6,7],8]

w,(x,y),z=list4

print('unapcked nested list elements')
print(w)
print(x)
print(y)
print(z)


t,*s,z=list4
print(l,s,z)


#Same things are applied to set as well, just replace list object to set object 

