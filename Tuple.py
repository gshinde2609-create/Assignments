#Packing &unpacking in tuple

#Packing - combaining/binding segrigated elemts as one entity.

a=100
b=300
c='Last'
tup=a,b,c

print('Combained elements as tuple -',tup)

#Unpacking - It process of seperating the indivisual object ad store in to seprate elements/veribales

a1,b1,c1=tup

print("Each element after unpacking -",a1,b1,c1)

#Tuple Unpacking with Asterisk (*) 
#*operator is used in tuple unpacking to grab multiple items into a list.
# This is useful to extract just a few specific elements and collect the rest together.
tup1=(1,2,3,4,5,6,7)
x,*y,z=tup1

print('Using * operator -',x,y,z)

y,*p=tup1
print(type(y))

print(p)

# Explanation: x gets the first item,z gets the last item and *y collects everything in between into a list.