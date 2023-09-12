def zipper_lists(x,y):
    final = []
    y_count = 0
    x_count = 0
    while len(final) != len(x) + len(y):
        if x_count >= len(x)-1:
            for i in y[y_count:]:
                if x == None or x[-1] > i:
                    final.append(i)
                else:
                    final.append(x[-1])
                    x = x.clear()
                    final.append(i)
            break
        elif y_count >= len(y)-1:
            for j in x[x_count:]:
                if y == None or y[-1] > j:
                    final.append(j)
                else :
                    final.append(y[-1])
                    y = y.clear()
                    final.append(j)
            break
    
        if x[x_count] < y[y_count]:
            final.append(x[x_count])
            x_count += 1
        else:
            final.append(y[y_count])
            y_count += 1
    return final
def main():
    x = [1,2,7,9,16,20]
    y = [3,4,7,10,12]
    print(zipper_lists(x,y))
    print("[1, 2, 3, 4, 7, 7, 9, 10, 12, 16, 20]")
    x = [1,3,5,7,9,11]
    y = [2,4,6,8,10]
    print(zipper_lists(x,y))
    print("[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]")
    x = [1]
    y = [2,3,4,5,6,7,8,9,10]
    print(zipper_lists(x,y))
    print("[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]")
main()