from sys import argv
filename = argv[1]

with open(filename, "r") as fp:
    for line in fp:
        print(line, end = "")