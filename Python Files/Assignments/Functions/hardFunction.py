#################################################
#  Author: Ryan Krasinski
#  Date: 9/13/2021
#  harder_functions.py
#
# Make these happen using RECURSION!

from rt import close_enough, run_test, run_test_float
###################Problem 1################
def rectangle(m, n):
    """Precondition: m and n are nonnegative integers.
Postcondition:  returns a string containing
a rectangle of *s to the screen that 
has m rows and n columns"""
    row = "*"*n
    if (m == 0):
        return ""
    return row + "\n" + rectangle(m-1,n)
    #pass

###################Problem 2################
def power(base, exp):
    """prec:  base is a number, exp is an integer`
postc: computes base**exp from scratch (no using libraries
or built-in functions).  Pay attention to the case where exp < 0!"""
    if(exp == 0):
        return 1
        #print(-1 + base + power(base,exp-1))
    elif (exp < 0):
        return power(1/base,-exp)
    else:
        return base*power(base,exp-1)
        

###################Problem 3################
def convert_to_binary(n):
    """prec: n is an integer
    postc: retrns a string containing a binary representation of n.
    return """
    if n == 0:
        return ""
    else:
        return str(convert_to_binary(n//2)) + str(n%2)
###################Problem 4################
def sum_of_digits(n):
    """precondition: n is an integer
postcondition:  returns the sum of the digits of n.  You should
be able to take negative input; in such cases disregard the - sign.  """
    if n == 0:
        return 0
    else:
        return n%10 + sum_of_digits(n//10)
###################Problem 5################
def function(k):
    return k + 1
def super_summer(f, n):
    """precondition: f is a function that is defined for all nonnegative
integers.
postcondition:  returns sum(f(k), k = 1..n) """
    if n != 0:
        return f(n) + super_summer(f, n-1)
    else:
        return 0
###################Problem 6################
def reverse_string(x):
    """prec: x is a string
    postc:  return a string containing x reversed."""
    #Easy way: return x[::-1]
    if x == x[::-1]:
        return x

    y = x[-1]
    if (x == y[::-1]):
        return y
    else:
        return y + reverse_string(x[:len(x)-1])
###################Problem 7################
def sum_from(n, x):
    """prec:  n is an integer, x is a list of integers.
postc: returns a sublist of x whose sum is n if it exists
and the graveyard object None otherwise.  """
    #base cases
    if (n == 0):
        return []
    if(x == []):
        return None
    
    first = x[0]
    rest = x[1:]
    first_try = sum_from(n,rest)
    if first_try != None:
        return first_try
    second_try = sum_from(n-first,rest)
    if second_try != None:
        return [first] + second_try
    return None

def main():
    # run your tests in this main function
    print("###################Problem 1################")
    test = [2, 2]
    expected = "**\n**\n"
    run_test(rectangle, expected, test)
    test = [5, 5]
    expected = "*****\n*****\n*****\n*****\n*****\n"
    run_test(rectangle, expected, test)
    test = [2, 4]
    expected = "****\n****\n"
    run_test(rectangle, expected, test)
    print("###################Problem 2################")
    test = [2,0]
    expected = 1
    run_test(power, expected, test)
    test = [2,2]
    expected = 4
    run_test(power, expected, test)
    test = [2,1]
    expected = 2
    run_test(power, expected, test)
    test = [2,-1]
    expected = 0.5
    run_test(power, expected, test)
    print("###################Problem 3################")
    test = [8]
    expected = "1000"
    run_test(convert_to_binary, expected, test)
    test = [320]
    expected = "101000000"
    run_test(convert_to_binary, expected, test)
    print("###################Problem 4################")
    test = [320]
    expected = 5
    run_test(sum_of_digits, expected, test)
    test = [123]
    expected = 6
    run_test(sum_of_digits, expected, test)
    test = [1]
    expected = 1
    run_test(sum_of_digits, expected, test)
    print("###################Problem 5################")
    test = [function, 1]
    expected = 2
    run_test(super_summer, expected, test)
    test = [function, 10]
    expected = 65
    run_test(super_summer, expected, test)
    print("###################Problem 6################")
    test = ["abc"]
    expected = "cba"
    run_test(reverse_string, expected, test)
    test = ["racecar"]
    expected = "racecar"
    run_test(reverse_string, expected, test)
    test = ["Ryan"]
    expected = "nayR"
    run_test(reverse_string, expected, test)
    test = ["ernie"]
    expected = "einre"
    run_test(reverse_string, expected, test)
    print("###################Problem 7################")
    n = 4
    x = [1,2,3,4,5,6]
    out = sum_from(n,x)
    print("PASS" if sum(out) == n else "FAIL")
    x = [1,2,4,8,16,32,64]
    n = 100
    out = sum_from(n,x)
    print("PASS" if sum(out) == n else "FAIL")

main()