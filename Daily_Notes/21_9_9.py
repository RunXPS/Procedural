#I'm my own grandpa
def printListFwd(x):
    if x == []:
        return 
    first = x[0]
    rest = x[1:]
    print(first)
    printListFwd(rest)

def printListBack(x):
    if x == []:
        return 
    first = x[0]
    rest = x[1:]
    printListBack(rest)
    print(first)
    

x = list(range(100))
x = [1,2,3,4]
printListFwd(x)
printListBack(x)

#binomial recursion
#c(n, k) = numer of subsets size k in in a set of size n
#c(n,0) = 1
#c(n,1) = n
print("")
def choose(n,k):
    if k > n or k < 0:
        return 0
    if k == 0 or k == n:
        return 1
    return choose(n-1,k-1) + choose(n-1,k)

print(choose(4,2))
#There are 4 ^ different intances of objects (abcd) or (1234) -> all different
#How many combinations of 2 of the 4 objects are there (ab, ac, ad, bc, bd, cd) or  (12, 13, 14, 23, 24, 34)
print(choose(52,5))
#how many hands of 5 cards are there in a 52 deck of cards

def nag():
    x = input("Enter a number 1-10: ")
    x = int(x)
    if 1 <= x <= 10:
        print (f"You chose {x}.")
        return
    nag()
#"Idiot proof" -> calls itself until condition is met

nag()