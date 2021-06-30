#1292. 쉽게 푸는 문제 

import sys

A,B = map(int, sys.stdin.readline().split(" "))

lis = [] 
for x in range(1,B+1):
    for y in range(x):
        lis.append(x)

    
sum = 0 
for i in range(A,B+1):
    sum += lis[i-1] 

print(sum)


