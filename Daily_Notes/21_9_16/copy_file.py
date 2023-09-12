from sys import argv
import os
## atomicity of purpose
## this function does one thing : it copies a file
def copy_file(donor, reciprient):
    with open(donor, "r") as fp_in:
        with open (reciprient, "w") as fp_out:
            fp_out.write(fp_in.read())

#malformed invocation ==>
if len(argv < 3 ):
    print("Usage is python copy.py donor recipient")
    quit()

donor = argv[1]
reciprient = argv[2]

#donor does not exist.
if not os.path.exists(donor):
    print(f"File {donor} does not exist")
    quit()

if os.path.exists(reciprient):
    reply = input(f"Do you want to clobber {reciprient}? (y/n): ")
    if reply[0].lower() == "y":
        copy_file(donor, reciprient)
    else:
        print("--session ending--")
        quit()
copy_file()
#cobbering

