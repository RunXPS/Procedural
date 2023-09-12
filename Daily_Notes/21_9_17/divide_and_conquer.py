n = int(input("Enter N: "))
a = 0
b = n - 1
x = a
y = b
r = b
print(f"\t \n", str(a), " ", str(b))
while(b > 1):
    r //= 2
    while (x < n - 1):
        print(" ", x, end=" ")
        y = x + r
        print(" ", y, end=" ")
        x = y + 1
    x = a
    b = r
    y = b
    print("\n")