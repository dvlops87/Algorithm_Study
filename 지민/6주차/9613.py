#9613. GCD의 합 

import math
import sys 
from itertools import combinations


for _ in range(int(input())):
    A = list(map(int, sys.stdin.readline().split(" ")))
    a = A[1:]
    lis = list(combinations(a,2))

    sum = 0 
    for x in lis:
        sum += math.gcd(x[0], x[1])

    print(sum)
