import random
def swap(x,j,k):
    if j != k:
        x[j], x[k] = x[k], x[j]

def adjacent_neighbors(x):
    """ 
    1) looks at last two
    2) swaps if first is bigger
    3) move pointer back one 
    4) repeat
    """
    p = len(x)-1
    while p > 0:
        largest = 0
        index = p - 1 
        if x[p] < x[index]:
            swap(x, p, index)
        p -= 1
    return x

def trickle_down(x):
    """ 
    pointer starts at x[1]
        everything left is sorted
        everything right is "a jungle"
    1) move pointer
    2) if first is bigger than the new, swap
    3) check the new with the next until the left is sorted
    4) repeat
    """
    p = 1 
    while p < len(x):
        i = p
        p += 1
        while i > 0:
            if x[i] < x[i-1]:
                swap(x, i, i-1)
            i -=1
        
    return x

def main():
    x = [1,3,6,2,8]
    print(x)
    print(adjacent_neighbors(x))
    x = list(range(15))
    random.shuffle(x)
    print(x)
    print(trickle_down(x))
main()