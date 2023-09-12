def swap(x,j,k):
    if j != k:
        x[j], x[k] = x[k], x[j]
def minisort(x):
    """x is a list
    put pointer (p) at first element
    1) find smallest element
    2) swap first with smallest element
    3) move pointer over 1
    4) repeat until elements are sorted
    """
    p = 0
    while p < len(x):
        temp = x[p]
        for i in x[p:]:
            if temp > i:
                temp = i
        if temp == x[p]:
            p += 1
        else:
            swap(x,x.index(temp),p)
            p += 1
    return x
def morrison_minisort(x):
    p = 0
    while p < len(x):
        #find index of min value of x[p:]
        smallest = x[p]
        index = p
        for j in range(p+1,len(x)):
            if smallest > x[j]:
                smallest = x[j]
                index = j
        swap(x, p, index)
        p += 1

def main():
    x = [1,3,2,5,4]
    print(x)
    print(minisort(x))
    x = [11,63,42,5,94]
    print(x)
    print(minisort(x))
main()