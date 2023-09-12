####################################
# Author: Ryan Krasinski
#  Date created: 30 Aug 2021
#  Date last modified: 30 Aug 2021
#  Program: stringPlay.py
# 
####################################

###############Problem 0#################
#   Example problem to show how this works.
#   arg is a lower-case string with at least two instances
#   of the letter q
#   Find the substring of arg between the first and last q
#########################################

arg = "quoque"
start = arg.find("q")
end = arg.rfind("q")
my_result = arg[start + 1: end]
result = "uo"  ##this is my given result
print(result == my_result)  ##prints True if you succeeded.
arg = "miasma"
start = arg.find("a")
end = arg.rfind("a")
my_result = arg[start + 1: end]
result = "sm"  ##this is my given result
print(result == my_result)  ##prints True if you succeeded.

###############Problem 1#################
#   Remove all instances of the lower-case letter
#   s from a string.  
#########################################

arg = "sissyphus"
# your code goes here.
result = "iyphu"
arg = "sissyphus"
arg = arg.replace('s','')
print(result == arg)

###############Problem 2#################
#   arg is guaranteed to have at least two letters
#   and be an alphabetical string
#   Create a string with the first and last letters of arg.
#########################################

arg = "heinous"
decoy = list(arg)[0] + list(arg)[len(arg)-1]
arg = decoy
result = "hs"
print(arg == result)

arg = "Washington"
result = "Wn"
decoy = list(arg)[0] + list(arg)[len(arg)-1]
arg = decoy
print(arg == result)
###############Problem 3#################
#   head has an even number of letters
#   tail has an even number of letters
#   Create a string whose first half is the first
#   half of head and the second half of tail.
#########################################

head = "cerebellum"
tail = "wagger"
result = "cerebger"

total = head[0:len(head)//2] + tail[len(tail)//2:len(head)-1]
print(result == total)

###############Problem 4#################
#   arg is any string
#   Find out how many times the letter b occurs 
#   in arg, case INsensitive
#########################################

arg = "Babbage"
result = 3
print((arg.lower()).count("b") == result)

###############Problem 5#################
#   arg is any string
#   Find out how many times the letter b occurs 
#   in the first 10 letters of arg, case INsensitive
#########################################

arg = "Babbage"
result = 3
print((arg.lower()).count("b",0,10) == result)

arg = "flibbertygibbet"
result = 2
print((arg.lower()).count("b",0,10) == result)


###############Problem 6#################
#   arg is any string
#   center the string in a string of length 30
#   padded with !s.  
#   if the string has more than 30 characers, just
#   display it.  (no conditional logi on your part needed)
#########################################

arg = "wabbit"
result = "!!!!!!!!!!!!wabbit!!!!!!!!!!!!"
decoy = "!"*((30-len(arg))//2) + arg + "!"*((30-len(arg))//2)
if (len(decoy) != 30):
    decoy += "!"
print(decoy == result)

###############Problem 7#################
#   arg is any string
#   get rid of all of the whitespace on the left, if any
#   replace any spaces on the right with @s.
#########################################

arg = "        wabbit    "
result = "wabbit@@@@"

decoyString = arg.strip(" ")
first = decoyString[0]
decoyTuple = arg.partition(decoyString[0])
arg = str(decoyTuple[1]) + str(decoyTuple[2])
arg = arg.replace(" ", "@")
print(arg == result)