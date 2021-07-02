A, B = map(int, input().split())

a = []
a.append(0)
for i in range(1000):
    for j in range(i):
        a.append(i)

sum = 0
for i in range(A, B+1):
    sum += a[i]
print(sum)

#다시 보기