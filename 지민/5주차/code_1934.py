#최소공배수

import math

for _ in range(int(input())):

    A,B = map(int, input().split(" "))
    print((A*B)//math.gcd(A,B))