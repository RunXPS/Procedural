def square (x:int) -> int:
    return x*x
def dublin (x:int) -> int:
    return 2*x

print("2 times 4 is: " + str(dublin(4)))
print("here is an error:" + dublin("brains"))

def fun(x,y):
    return 3*x + 2*y
x = 13
print(fun(4+7, x-5))

#positional arguement ==> inputting f(5,4) and f(4,5) give you 54 and 45, very different answers
def f(x,y):
    return x + y*10

#keyword arguement ==> can call upon initialized keywords 
def g(x = 0, y = 0, z = 0):
    return x + 10*y + z

#print 111
print(g(1,1,1))
#print 500
print(g(z=500))

#Starguments
def f(*x):
    return sum(x)
def abc(y, *x):
    """ returns the sum of the numbers passed to it
    BUT it requires at least one number """
    return y + sum(x)

print(f(1,2,3,4,5,6,7))
print(abc())
print(1,2,"cat", True, [1,2,3], print)

x = [1,2,4,7,-9]
#prints the maximum value
print(max(x))
#prints the maximum absolute value, using a "key" to determine perameters
print(max(x,key = abs))

#assigning to literals
a = 5
b = "cows"
c = 4.9
#"lambda" makes a function in a variable
f = lambda x: x*x*x
print(f(5))

def makeTable(x,f):
    print("<table>")
    print("<tr><th>x</th><th>f(x)</th></tr>")
    for item in x:
        print(f("<tr><th>item</th><th>f(item)</th></tr>"))
    print("<table>")

x = list(range(10))
print()