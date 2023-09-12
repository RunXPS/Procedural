from sys import argv
for filename in argv[1:]:

    #filename = argv[1]
    with open(filename, "r") as fp:
        print(fp.read(), end=" ")