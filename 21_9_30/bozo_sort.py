import random
#from sys import argv

def is_in_order(x):
    for k in range(len(x)-1):
        if x[k] > x[k+1]:
            return False
    return True

def bozo_sort(x):
    """ see if the list is in order
    if it is return
    if not, shuffle the list and repeat
    """
    if is_in_order(x):
        return
    while(not is_in_order(x)):
        random.shuffle(x)

#n = int(argv[1])
n = 10
x = list(range(n))
random.shuffle(x)
print(x)
bozo_sort(x)
print(x)