
#Set methods



s1=set() #Created empty set

#add() is used to add elements in set

print('Set before adding any element -',s1)
s1.add(1)
s1.add('A')
s1.add(2)
s1.add(4)

print('Set After adding an elements -',s1)

'''
If you try to add any mutable object directly to set then it will 
not accept it wil throw error
s2={00,12,23}

s2.add(set(l))
#print(s2)

# t=(1,2,3)
# s2=(00,12,23)

# s2.add(t[1])
# print(s2)


'''


#update() Methods to update set 
#update method will need the ietrtable object as arrgument 

l=[8,9,10] #list object 
s1.update(l)

print('Set after updating -',s1)

#Methods to delete elemnts from set

#pop() is used to delete element from list but the element will be deleted randomly 
# pop() will retrun the deleted element 

deleted_element=s1.pop()

print('Deleted element -',deleted_element)

print("Set after using pop method =",s1)

#discard() method is used to delete the elements from set
# required argument is element which you want to delete

s1.discard(10)

print("Print set after deleting element using discard() - ",s1)

#remove() method 

s1.remove(9)
print("Print set after deleting element using remove() - ",s1)


#copy () is used to make the copy of set

s2=s1.copy()
print('new set created using copy method=',s2)

#clear() clear method will clear everything from set and will ake it empty 

s2.clear()
print("Set after using clear method =",s2)
