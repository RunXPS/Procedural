from sys import argv
filename = argv[1]
with open(filename, "r") as fp:
    print(fp.read(), end=" ")