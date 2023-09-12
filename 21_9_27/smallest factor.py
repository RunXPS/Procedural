def smallest_factor(n):
    """ Precon: n is an interger, n >= 1.
    of m == 1, return 1
    return the smallest factor of n that is >= 2
    """
    if n == 1:
        return 1
    for i in range(n):
        if i < 2:
            pass
        else:
            if n % i == 0:
                return i
    return n

def smallest_factor2(n):
    """ Precon: n is an interger, n >= 1.
    of m == 1, return 1
    return the smallest factor of n that is >= 2
    """
    if n == 1:
        return 1
    for i in range(2, n + 1):
        if n % i == 0:
            return i

def smallest_factor3(n):
    """ Precon: n is an interger, n >= 1.
    of m == 1, return 1
    return the smallest factor of n that is >= 2
    """
    if n == 1:
        return 1
    if n % 2 == 0:
        return 2
    i = 3
    while i * i < n:
        if n % i == 0:
            return i
        i += 2
def prime_factorization(n):
    """ precon: n >= 1. if n == 1, return []
    otherwise, return a list containing the prime factors of n
    """
    factors = []
    prime_factors = []
    if n == 1:
        return []
    
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
            print(factors)
    for j in factors:
        is_prime = True
        k = 3
        while is_prime == True:
            if j%k == 0:
                is_prime = False
            k +=2
        if is_prime == True:
            prime_factors.append(j)
            print(prime_factors)
    return prime_factors

def main():
    x = 8
    print(f"The smallest factor of {x} is {smallest_factor(x)}")
    x = 5
    print(f"The smallest factor of {x} is {smallest_factor(x)}")
# ----------------------------------------------------------------- #
    x = 111
    print(f"The smallest factor of {x} is {smallest_factor(x)}")
    x = 1
    print(f"The smallest factor of {x} is {smallest_factor(x)}")
    x = 8
    print(f"The smallest factor of {x} is {smallest_factor(x)}")
    x = 215
    print(f"The smallest factor of {x} is {smallest_factor(x)}")
    x = 997
    print(f"The smallest factor of {x} is {smallest_factor(x)}")
    x = 10000007
    print(f"The smallest factor of {x} is {smallest_factor(x)}")

    x = 10000007
    print(f"The smallest factor 3.0 of {x} is {smallest_factor3(x)}")

    x = 9
    print(f"The prime factors of {x} is {smallest_factor3(x)}")
main()