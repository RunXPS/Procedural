from math import log, e, pi, sin, cos, asin
#from run_tests import close_enough, run_test, run_test_float

## you can now use log(x) for the natural log of x.
## You can only use the imported functions that I specify.

###################Problem 1################
def greet(name):
    """prec:  name is a keyword argument with default value "Stranger"
    postc: returns the string Hello, name!"""  
    return "Hello, " + name + "!"
###################Problem 2################
def log_base(x, b = -1):
    """prec:  x > 0 and b > 0 is a keyword argument
    postc: use the change-of-base formula to compute 
    the logarithm of x with base b.  The default is that
    the natural log of x is returned."""
    if b == -1:
        return log(x)
    else:
        return log(x, b)
###################Problem 3################
def truncate(s, n = 3):
    """prec:  s is a string, n is a nonnegative integer
    and a keyword argument.  if len(x) > s return s; otherwise
    truncate at n.  By default, n = 3."""
    if (n > len(s)):
        return s
    else:
        return s[:n] 
###################Problem 4################
def protean_sin(x, radians = True):
    """prec: x is a number, radians is a boolean and a
    keyword argument.  
    postc: returns sin(x) using radians if radians is True
    and sin(x) in degrees if radians is false.
    The default is True"""
    if radians == True:
        return sin(x)
    else:
        return sin(x)*(180/pi)
###################Problem 5################
def protean_asin(x, radians = True):
    """prec: x is a number, -1 <= x <= 1.
    radians is a keyword argument.  
    postc: returns asin(x) using radians if radians is True
    and arcsin(x) in degrees if radians is false.
    The default is True."""
    if radians == True:
        return asin(x)
    else:
        return asin(x)

###################Testing###################
def run_test(expected, test):
    if expected == test:
        return "Pass"
    else:
        return "Fail"
def main():
    print("*************** Problem 1 Tests ***************")
    test = ["Kyle"]
    test = greet(name="Kyle")
    expected = "Hello, Kyle!"
    print(run_test(test, expected))
    #run_test(greet, expected, name=test)
    test = ["Ryan"]
    test = greet(name="Ryan")
    expected = "Hello, Ryan!"
    print(run_test(test, expected))
    #run_test(greet, expected, name=test)
    print("*************** Problem 2 Tests ***************")
    test = [5, 5]
    test = log_base(5,5)
    expected = 1.0
    print(run_test(test, expected))
    #run_test(log_base, expected, test)
    test = [5]
    test = log_base(5)
    expected = 1.6094379124341003
    print(run_test(test, expected))
    #run_test(log_base, expected, test)
    test = [5, 2]
    test = log_base(5,2)
    expected = 2.321928094887362
    print(run_test(test, expected))
    #run_test(log_base, expected, test)
    print("*************** Problem 3 Tests ***************")
    test = ["Susan", 3]
    test = truncate("Susan",3)
    expected = "Sus"
    print(run_test(test, expected))
    #run_test(truncate, expected, test)
    test = ["Susan", 3]
    test = truncate(n=3, s="Susan")
    expected = "Sus"
    print(run_test(test, expected))
    #run_test(truncate, expected, test)
    test = ["Danny"]
    test = truncate(s="Danny")
    expected = "Dan"
    print(run_test(test, expected))
    #run_test(truncate, expected, test)
    test = ["Elephant", 100]
    test = truncate("Elephant",100)
    expected = "Elephant"
    print(run_test(test, expected))
    #run_test(truncate, expected, test)
    print("*************** Problem 4 Tests ***************")
    test = [1]
    test = protean_sin(1)
    expected = 0.8414709848078965
    print(run_test(test, expected))
    #run_test(truncate, expected, test)
    test = [1, False]
    test = protean_sin(1, False)
    expected = 48.21273601220948
    print(run_test(test, expected))
    #run_test(truncate, expected, test)
    test = [1, False]
    test = protean_sin(radians=False,x=1)
    expected = 48.21273601220948
    print(run_test(test, expected))
    #run_test(truncate, expected, test)
    print("*************** Problem 5 Tests ***************")
    test = [1, False]
    test = protean_sin(radians=False,x=1)
    expected = 1.5707963267948966
    print(test)
    print(run_test(test, expected))
    #run_test(truncate, expected, test)
    
main()