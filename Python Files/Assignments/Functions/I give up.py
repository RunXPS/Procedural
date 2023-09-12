def sum_from(n,x):
    final = []
    for i in x:
        for j in range(len(x)-1):
            if i + j == n:
                final.append(i)
                final.append(j)
    return final

print(sum_from(4, [1,2,3,4,5,2]))