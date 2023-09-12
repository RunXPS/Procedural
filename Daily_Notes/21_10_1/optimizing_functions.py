def butter(f,x):
    """prec: f is a function defined on the elements of x
    returns a list that if c f-ed
    """
    out = []
    for k in x:
        out.append(k)
    return out
def better_butter(f,x):
    return [f(k) for k in x] 
def trimmed_sum(x,limit):
    """prec: x is a numerical list, limit is a number
    postc: returns the sum of all elements of x <= limit
    """
    total = 0
    for k in x:
        if k <= limit:
            total += k
    return total
def better_trimmed_sum(x,limit):
    return sum([k for k in x if x <= limit])

def main():
    print(butter(lambda x: x*x*x, [1,2,3,4]))
    print(better_butter(lambda x: x*x*x, [1,2,3,4]))
main()