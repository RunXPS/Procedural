arg = "        wabbit    "
result = "wabbit@@@@"

decoyString = arg.strip(" ")
first = decoyString[0]
decoyTuple = arg.partition(decoyString[0])
arg = str(decoyTuple[1]) + str(decoyTuple[2])
arg = arg.replace(" ", "@")
print(arg == result)