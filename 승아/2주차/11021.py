times = int(input())

for i in range(times):
    i += 1
    a, b = map(int, input().split())
    print("Case #%d: %d" %(i, a+b))