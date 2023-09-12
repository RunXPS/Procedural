def square(x):
    """
    precondition: x is a number
    postcondition: returns the square of x
    """
    return x*x

def swap (x, j, k):
    """
    prec: x is a list; j & k are intergers in range (len(x))
    postc: items at position j & k are swapped
    """
    x[j], x[k] = x[k], x[j]

def elzippo (x):
    x = [0, 0, 0, 0]
    return x

#x = [5,6,7,8]
#print(x)
#swap(x, 0, 1)
#print(x)
#elzippo(x)
#print(x)
#b/c functions are always "handed" a copy of their input, changes to the input will not effect the actual object. 

def foo(x):
    if x < 0:
        x = -x
    return x

def dusty(age):
    out = ""
    if age < 21:
        out = "get outta here punk!"
    elif age > 65:
        out = "Shall I cash yer Soshal, Geezer??"
    else:
        out = "Name your poison boy."
    return out

print(dusty(13))