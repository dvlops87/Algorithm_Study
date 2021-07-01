times = int(input())

for i in range(times):
    i += 1
    a, b = map(int, input().split())
    print("Case #%d: %d + %d = %d" %(i, a, b, a+b))