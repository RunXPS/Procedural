import math
class point(object):
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return f"{self.x},{self.y}"
    def __eq__(self, other):
        if type(other) != point:
            return False
        return self.x == other.x and self.y == other.y

    def distance_to(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)
    def reflect_across_x(self):
        return(self.x,-self.y)

p = point(3,4)
s = point(3,4)
q = point(0,0)
print(f"P == S: {p == s}")
print(f"Distance to points: {p.distance_to(q)}")
#print(p)
print(f"Reflect across X: {p.reflect_across_x()}")