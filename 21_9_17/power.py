from rt import close_enough, run_test, run_test_float
def power_rec(base, exp):
    """prec:  base is a number, exp is an integer
    postc: retuerns base**exp using a recursive version of the 
    divide and conquer power algorithm"""  
    if exp == 0:
        return 1
    if exp < 0:
        base = 1/base
        exp = -exp
        #return power_rec(base, exp)
    if exp > 1:
        return base*power_rec(base,exp-1)
    else:
        return base
def power_iter(base, exp):
    """prec:base is a number, exp is an integer
    postc: returns base**exp using an itearative version of the 
    divide and conquer power algorithm"""  
    #Base Cases
    if exp == 0:
        return 1
    if exp < 0:
        base = 1/base
        exp = -exp
    #Needed Variables
    divide = [[] for i in range(exp)]
    total = 1
    #Divide
    for i in range(exp):
        divide[i] = base
    #Combine
    for i in range(len(divide)):
        total *= divide[i]
    
    return total

def main():
    ##run tests here
    run_test(power_iter, 1024, [2, 10])
    run_test(power_iter, 1/1024, [2, -10])
    run_test(power_iter, 9, [3, 2])
    
    run_test(power_rec, 1024, [2, 10])
    run_test(power_rec, 1/1024, [2, -10])
    run_test(power_rec, 9, [3, 2])
main()