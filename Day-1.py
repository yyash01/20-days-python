#if 5>2:
	#print("five is greator than two!")


#PYTHON VARIABLES--------------
x = 5
y = "yash jain"
print(x)
print(y)
# a variable name cannot start with a number.
#variable name are case sensitive.
#A variable name must start with a letter or the underscore character

x,y,z = "red","orange","yellow"
a = str(6)
print(x+" "+y+" "+z+" "+a)
#-------------------------------------------- 

#DEFbbbYNING A FUNCTION

#----------------------------------------------------------------
#Variables that are created outside of a function
# (as in all of the examples above) are known as global variables.


a = "good"
def myfirst_func():
	print("python is "+a)

myfirst_func()
#-----------------------

#DEFYNING VARIABLE INSIDE A FUNCTION
def sec_func():
	a = "awesome"
	print("python is "+a)

sec_func()

#LIST IN PYTHON EXAMPLE ----   x = ["apple", "banana", "cherry"]

#DICTIONARY IN PYTHON--------x = {"name" : "John", "age" : 36}

#SET IN PYTHON-----------x = {"apple", "banana", "cherry"}

#BOOL-------------x = True

################################################################

#PYTHON NUMBERS-------------------------------------------
x = 1    # int
y = 2.8  # float
z = 1j   # complex
#To verify the type of any object in Python, use the type() function
print(type(x))
print(type(z))
#You cannot convert complex numbers into another number type.
b = "Hello, World"
print(" ")
print(b[7])

#Specify the start index and the end index,
# separated by a colon, .
print(b[0:5]) #----------to return a part of the string
print(b[-5:-1])# -4 se lekr  -1 is included.
print(b[-8:-1])#-7 se lekr -1 is included.

print("\n")#\n is new line character.

a = "Hello, World!"
print(a.replace("H", "J"))
print("\nHello\nworld")

a =200
b = 100
if b>a:
	print("b is greator than a")
else:
	print("a is greator than b")

x = 15
y = 2
z = str(x//y) ##the floor division // rounds the result down to the nearest whole number
print("\n"+z)


#######################################################################################################################33333333333333
#
#
#----------Python Collections (Arrays)--------------------------

# *list = a collection which is ordered and changeable. allows duplicate members.
#In Python lists are written with square brackets.

thislist = ["apple", "banana", "cherry"]
print("\n"+thislist[1]) #indexing is started from 0
#range of indexes
print(thislist[0:2]) #last index is not printed

print("\n")
#looping first time using the list
first_list = ["apple","oranges","mango"]
for x in first_list:
	print(x)
print("\n")
#checking the item is present or not
if "mango" in first_list:
	print("YES 'mango' is present the list mentioned above ")

#to check the length of list
print(len(thislist))

#to insert item at any given position in the list
thislist.insert(0,"lemon") #to insert at starting position
print(thislist)

#You cannot add items to a tuple\

#using if else functions in python
b = 4
c = 33
if b>c:
	print("B is greator than c")
elif b==c:
	print("B is equal to c")
else:
	print("\nC is greator than b")


a = 20
b = 33
if a>b: print("A>B") 
else:print("B>A")

#The --[and]-- keyword is a logical operator, and is used to 
#combine conditional statements
a = 200
b = 33
c =400
if (a>b and c>a):
	print("\nBoth condition are true")
if (a>c):
	print("true A>C")
elif(a>b):
	print("A>B")


#applying while loop
i = 1
while (i<6):
	if(i==3): #CONTINUE TO NEXT ITERATION IF i IS 3
		continue
	print(i*2)
	i = i+1
