#Dictionary is set of elements with format of key:value

#How create dictionary 

#using emprty curly braces
d1={}
print("Type of empty dict-",type(d1)) #empty curly braces in python considered as dictionary 

d2={'Name':'Gorakh','Age':34,'Skills':'Software Development'}

print("Print dict created with values -",d2)

#Using built in funcation 
d3=dict({1:'abc',2:100,'A':7})

print('Print dict created using built in funcation -',d3)

#Methods of Dictionary 

#Add/update elements in dict

#1.update() - it will used to add/update the elements 

d1.update({4:100,5:500,6:600}) # Added key:value directly 
print('Print the dict after update() -',d1)

# add another dictionry using update method.

d1.update(d3)
print("dict afte adding another dict using update method-",d1)

#update existing value of  existing key 

d1.update({5:'NewValue'})
print('Dict. after updating value of key 5 -',d1)

#2.setDefault() 
#it will work with key which is not there in dict. If the key is alrady there it will not perform any operation

d3.setdefault(3) #key 3 is not there in dict d3
print("Dict after using setdefault with new key -",d3)

#pass existing key as argument to setdefault()

d3.setdefault(2) #key 2 i already there in dict d3
print('Dict after setdeafult with existing key -',d3)

#Methods to access the dictionary elements 

#key() - it will give all keys from dictionry 

k=d3.keys()
print('Keys of dict using key() -',k)
print(type(k))

#values() - it will give all the values from dictionry 

v=d3.values()
print("All dict values using values()-",v)
print(type(v))

#get() - This will return the value of specified key. 
# key as argument is required

g=d3.get(1)
print("Vlaues of key 1 of dict using get()-",g)

#item() - it retruns all the elements of dict in tuple format, each tuple represents key:value pair

items_d=d3.items()
print('All the dict element using items()-',items_d)
print(type(items_d))

#Accessing the value using key directly 
kv=d3[2]
print('')

#Methods to delete the elements from dictionry 

#pop() - It will delete given key  entry(key:value) from the dictionry. key as parameter is required 

p=d3.pop(2)
print("Deleted entry from dict using pop()-",p)
print('Dict after deleteing key 2-',d3)

#popitem() -  it will remove and return the last inserted or last entry from dict

pi=d3.popitem()
print('Last entry deleted from dict using popitem()-',pi)
print('Dict after deleting last enrty -',d3)

