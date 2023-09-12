def function(x):
    return x - 1

def find_root (a, b, tol, f):
    """ Precond: [a,b] is an interval and f is continuous on [a,b] 
        tol is a positive tolerance for error
        f changes sign on [a,b]
        returns a value in the interval that is within tol of the actual root.
    """
    while abs(b-a) > 2*tol:
        mid = (b+a)/2
        if f(mid)*f(a) < 0:
            b = mid
        else:
            a = mid
    return (b+a)/2

def main():
    print("when x is 5, y is " + str(function(5)))
    print("The root of y = x - 1 is " + str(find_root(0,3,0.0001,function))) #Needs to be 1
main()