# Total Import
#>>> import math
#Selective import
#>>> from math import sin, cos
import sys
def factorial(n):
    if n in [0,1]:
        return 1
    return n*factorial(n-1)

sys.setrecursionlimit(10003)
print(factorial(100))