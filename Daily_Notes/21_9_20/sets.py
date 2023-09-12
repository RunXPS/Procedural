s = {1,2,3,4,5,6,7,8,9,10}
t = {2,4,6,8,10}
s = set(s)
t = set(t)

print("s & t: " + str(s & t))
print("s | t: " + str(s | t))
print("s.union(t)/ sUt: " + str(s.union(t)))
print("s.intersection(t)/ sNt: " + str(s.intersection(t)))
print("s - t: " + str(s - t))
print("t - s: " + str(t - s))
print("s ^ t: " + str(s ^ t))
print("s & t: " + str(s & t))
#sets cannot be sorted
#allow for rapid access to elements
