#Typecasting - converting one datatype into a certain data type in order to perform the required operation by users.
# We will see various techniques for typecasting. There can be two types of Type Casting in Python:

# Implicit Type Conversion - built in conversion done by python dynamicly 
# e.g - a=10
# b=2.5
# c=a+b
# Here c is automatically converted to flot as result will be in float


# Explicit Type Conversion
#  Explicit type conversion is when the programmer manually changes a value’s data type using built-in type casting functions, 
# usually when automatic conversion is not possible or a specific type is needed.

#Assignment: Create a simple bill of Grocery. Take 3-4 inputs and print the final bill

sugar=40
milk =72
coffe=600
daal=120
rice =80

customer=str(input('Customer Name -'))
sugar_q=float(input("Enter sugar quantity in kg-"))
milk_q=float(input('Enter milk quantity in liter-'))
coffe_q=float(input("Enter Coffe quantity in kg-"))
daal_q=float(input("Enter Daal quantity in kg-"))
rice_q= float(input("Enter Rice quantity in kg-"))

st=sugar*sugar_q
mt=milk*milk_q
ct=coffe*coffe_q
dt=daal*daal_q
rt=rice*rice_q

print("******* Bill Details **********")
print('Customer -\t\t',customer)
print('_____________________________________')
print('Item \t\t Amount')
print('Sugar\t\t',st)
print('Milk\t\t',mt)
print('Coffee\t\t',ct)
print('Daal\t\t',dt)
print('Rice\t\t',rt)
print('_____________________________________')
print('Total Amount\t\t',st+mt+ct+dt+rt)

