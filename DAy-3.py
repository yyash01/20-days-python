#########################################################
#----------------COURSERA_LISTS-------------------------#
#-------------------------------------------------------#
#########################################################
print("\n")
print(range(5))
print("\n")

#BUILDING A LIST FROM SCRATCH
stuff = list()
stuff.append('book')
stuff.append('99')
stuff.append('43')
stuff.append('94')
print(stuff)
99 in stuff

############################# 

#SORTING IN LISTS
stuff.sort()
print(stuff)
abc = "with three words"
l = abc.split()
print(l)
print("\n")

#################################

#SPLITING IN STRINGS WITH ACCORDINGLY TO CHARACTERS
line = "first:thing:i:want:to:tell:is:yash:is:good:boy"
l = line.split(':')
print(l)


##################################################
###################################################
###################################################

#------------GOOD-QUESTION--of---COURSERA------#
#8.4 Open the file romeo.txt 
#and read it line by line.
#For each line, split the line into a list of words using the split() method. 
#The program should build a list of words. 
#For each word on each line check to see if the word is already in the list 
#and if not append it to the list. 
#When the program completes, sort and print the 
#resulting words in alphabetical order.
#You can download the sample data at

#ans---------------------------------------
fname = input("Enter file name: ")
fh = open('romeo.txt')
lst = list()
for line in fh:
    line = line.rstrip()
    wds = line.split()
    for x in range(len(wds)):
        if wds[x] not in lst:
        	lst.append(wds[x])

#maked a lst
lst.sort()
print(lst)

#--------------------------------------------#
