import math

class BigFraction(object):
    def __init__(self, num = 0, denom = 1):
        if denom < 0:
            num, denom = -num , -denom
        d = math.gcd(num,denom)
        num //= d
        denom //= d
        self.num = num
        self.denom = denom
    def __str__(self):
        return f"{self.num}/{self.denom}"
    def __eq__(self,other):
        if self is other:
            return True
        if type(self) != BigFraction:
            return False
        return self.num == other.num and self.denom == other.denom
    def __add__ (self, other):
        top = self.num*other.denom + self.denom*other.num
        bottom = self.denom*other.denom
        return BigFraction(top,bottom)
    def __sub__ (self, other):
        top = self.num*other.denom - self.denom*other.num
        bottom = self.denom*other.denom
        return BigFraction(top,bottom)

def main():
    f = BigFraction(3,4)
    print(f)
    g = BigFraction(-6,-8)
    print(g)
    h = BigFraction(1048576, 7776)
    print(g)
    a = BigFraction(1,3)
    b = BigFraction(1,2)
    print(a+b)
    print(b-a)

main()