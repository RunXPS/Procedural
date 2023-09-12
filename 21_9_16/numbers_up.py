school_items = ["calculator", "sheets", "lappy", "deodorant", "soap"]

for k in range(len(school_items)): #usually a code smell
    print(f"schoolitems[{k}] = {school_items[k]}")
print("***************************************")
for k, item in enumerate(school_items): #better way
    print(f"schoolitems[{k}] = {item}")
print("***************************************")
for k, item in enumerate(school_items, 1): #better way
    print(f"{k}.\t {item}")
