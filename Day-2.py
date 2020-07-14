#starting the second day.......

#i=1
#while (i<=6):
#	if(i==5):
#		continue
#	else:
#		if(i==4):
#			break
#	print(i)
#	i = i+1


#################################################
#FILE HANDLING IN .PYTHON.


#The key function for working with files in Python is the open() function.
#The open() function takes two parameters; filename, and mode.
#THERE ARE FOUR DIFFERENT METHODS OR !--MODES--! FOR OPENING A FILE:

#"r" - Read - Default value. Opens a file for reading, error if the file does not exist

#"a" - Append - Opens a file for appending, creates the file if it does not exist

#"w" - Write - Opens a file for writing, creates the file if it does not exist

#"x" - Create - Creates the specified file, returns an error if the file exists

################-##########################################################

#to open a file for reading it is enough to specify the name of the file:

#f = open("demo.txt","r") is same as 
#f = open("demo.txt")

###########################################################################

f =open("demo.txt","r")
print(f.read()) #TO PRINT THE DEMO FILE WHILE READING THE FILE DEMO.TXT
f.close()
########################################################################################

#You can return one line by using the readline() method:
print("\n")
f = open("demo.txt")
print(f.readline())
f.close()

print("\n")
# to return some part of the file we can use this method mentioned below
f = open("demo.txt","r")
print(f.read(6)) #1= H , 2= E,3= l,4= l,5= o,6= !
f.close()

############################################################################################
#To write to an existing file, you must add a parameter to the open() function:

#"a" - Append - will append to the *****end of the file*****

#"w" - Write - will **overwrite**any existing content
 
# 1st open the file for appendig
print("\n")
f = open("demo.txt","a")
f.write("\nNOW I ADDED THIS TEXT TO LAST OF FILE ! LOL !")
f.close()

#2nd open the file for reading again
f = open("demo.txt","r")
print(f.read())
print("\n")
f.close()
#################################################################################

#To delete a file, you must import the OS module, and run its os.remove() function:
import os
if os.path.exists("demofile.txt"):
	os.remove("demofile.txt")
else:
	print("THE FILE DOES NOT EXIST\n")

#to write something for code difficulty
f = open("demo.txt")
for line in f:
	line = line.rstrip()
	if not line.startswith('Hello!'):
		continue #if the line is not starting with "Hello!" then we will skip that line
	print(line)
f.close()

print("\n")

f = open("demo.txt")
for line in f:
 	line = line.rstrip()
 	if not "Hello!" in line:
 		print(line)
 	else:
 		continue
f.close()

################################################################################33333

#printing in line using string + integer $$$$$$$$$$$$$$$$$$$$$$$
print("\n")
x = 5
a = "yash jain is "

print(a,end=" ")
print(x)
