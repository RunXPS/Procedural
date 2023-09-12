from sys import argv
if len(argv) <3:
    print("Usage is python copy.py donor file recipient_file")
    print("Bailing.....")
    quit()
donor = argv[1]
reciprient = argv[2]
if os.path.exists(reciprient):
    x = input("Do you want to clobber {recipient}?")
    if (x[0].lower != "y"):
            print("Bailing.......")
            quit()
with open(donor, "r") as fp_in:
    with open(reciprient, "w") as fp_out:
        fp_out.write(fp_in.read())