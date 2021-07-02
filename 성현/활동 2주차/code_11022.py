cases = int(input())

for i in range(cases):
    a,b = map(int, input().split())
    and = a + b
    print("Case #%s: %s + %s = %s"%(i+1, a, b, and ))