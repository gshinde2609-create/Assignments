# Assignment:3
p = 'I love my India'
#using slicing access below values 

# Access my, India, I love, ove, love my, my India 

#Accessing my 
print(p[7:9])

#Accessing India
print(p[-5:]) #using negatuve indexing 
s=p.find("India")
#print(s)
print(p[s:]) #using find method

#accessing I love

s=p.find("my")
print(p[:s-1])

#Accessing ove
s=p.find('l')
s1=p.find('my')
print(p[s+1:s1-1])

#Accessing love my

s=p.find('love')
s1=p.find('India')
print(p[s:s1])

#accessing my India
s=p.find('my')
print(p[s:])

#Assignament4
 #remove spaces present in between
a='        J      A     9999  V  7777     A     '

b=a.replace(" ","")
print(b)

# Assignment:5 Check casefold()
# What is difference between casefold() and lower()

'''
casefold()- This return the string in lower case.
Converts uppercase letters to lowercase, including special characters and locale-specific cases.
Handles special cases like German "ß" (sharp S) correctly (e.g., "ß".casefold() => "ss"). 
'''
s1 = "ß"

s2 = s1.casefold()
print("Using casefold() - ",s2)

'''
lower()-	Converts uppercase letters to lowercase
Doesn't handle special or language-specific cases.
Basic lowercase conversion for general text processing.
'''

s3 = s1.lower()
print("Using lower() - ",s3)

