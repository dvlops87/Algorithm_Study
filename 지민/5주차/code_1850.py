#1850. 최대공약수

import math
import sys 

A,B = map(int, sys.stdin.readline().split(" "))


print(math.gcd(int(A),int(B))*"1")