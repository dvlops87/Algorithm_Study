a = [x for x in input().split()]
print(a)

for i in a:
    i = int(i)
    k = 2;
    print(i,k)
    while (i != 1):
        print(i)
        if (i % k) == 0:
            print(k)
            i /= k
        else:
            k += k