import random
def zipper(x, y):
    """ prec: x & y are homogeneous sorted list of a sortable type
    postc: returns a list that is combined and sorted from x and y
    in O(n) time
    """
    out = []
    p = 0
    q = 0
    while (p < len(x) and q < len(y)):
        if x[p] > y[q]:
            out.append(y[q])
            q += 1
        else:
            out.append(x[p])
            p += 1
    out += x[p:]
    out += y[q:]
    return out

def merge_sort(x):
    if len(x) <= 1:
        return x
    mid = len(x)//2
    first = x[:mid]
    second = x[mid:]
    return zipper(merge_sort(first), merge_sort(second))
def main():
    #Regular
    x = [1,2,5,8,9,13,28,64,189,210]
    y = [3,7,8,16,25,31,32,88]
    print(zipper(x,y))
    z = x + y
    z = sorted(z)
    print(z)
    #Swapped
    x = [3,7,8,16,25,31,32,88]
    y = [1,2,5,8,9,13,28,64,189,210]
    print(zipper(x,y))
    z = x + y
    z = sorted(z)
    print(z)
    #merge sort
    n = list(range(10))
    random.shuffle(n)
    print(n)
    print(merge_sort(n))
main()