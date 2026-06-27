#Create an empty list 

l=[]

# add element in list in normal way

'''l[0]=1 this will throw index related error
l[1]=2
'''
l.append(1)
print(l)
l.clear()


# Assignment: try to add str, list, tuple,set dict

#define all reuired objects.
s='i am string' #string object
list_1=[2,4,6] #list object
touple_1=(2,5,6,8) #touple object

set_1={1,2,3,5,4} #set object

dict_1={'name':'Gorakh','age':30}
#dict_2={1:2,3:4,1:'a'}

#add the object in list as it is  
#append(s) will add whole string as as single element in list where as 

l.append(s) 
l.append(list_1)
l.append(touple_1)
l.append(set_1)
l.append(dict_1)

print('output of append method =',l) #printing final list 



l1=[]
'''
Add the objects in list using extend in iteratuve way
l.extend(s) will add each char from string as single element in list

'''
l1.extend(s)
l1.extend(list_1)
l1.extend(touple_1)
l1.extend(set_1)
#l2=l1
l1.extend(dict_1)

print('Final output of extend() =',l1)

l2=[]
# Assignemnt: can we add a tuple to a list using extend?
#yes touple can be added in list using extend method

#new descovery 
# for dictonry we have follow surten steps 
# first bind the dict with list and the use extend method.
#e.g l1.extend([dict_1]) this will act same like append method
l2.extend([dict_1])

print('final result of list aving dict element=',l2)
