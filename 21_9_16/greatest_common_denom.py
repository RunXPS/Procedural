def gcd (a,b):
    
    if a < 0:
        a = -a
    if b < 0: 
        b = -b
    if a == 0 and b == 0:
        raise ValueError #kill calling idiot's program
    if a > b:
        a,b = b,a

    #number = 0
    q = b//a
    r = b%a

    if (r == 0):
        return a
    else:
        return gcd(a,r)

print(gcd(6,9))
print(gcd(35,147))
print(gcd(7776,1048576))