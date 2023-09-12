x = [1,2,3,4,5,6,7,8,9,10]
print("******************")
def sum_from(n, x):
    x.sort()
    y = []
    deleted = 0
    i = 0
    while i != len(x) - deleted:
        k = 0
        while k != len(x) - deleted:
            if i == k:
                pass
            elif x[i-1] + x[k-(1)] == n:
                y += x[i-1], x[k-1]
                x[i-1] = x.remove(x[i-1])
                x[k-1] = x.remove(x[k-1])
                deleted += 1

            else:
                pass
            k += 1
        i += 1
    return y

print(sum_from(7,x))


