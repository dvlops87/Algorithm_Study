# 2609. 최대공약수와 최소공배수
import math 

A,B = map(int, input().split(" "))

print(math.gcd(A,B))
print((A*B)//math.gcd(A,B))



# 망코드 
# def max(A,B):
#    global max 
#    max = 1 

#    for x in range():
#       if A%x == 0 and B%x ==0:
#          A = A//x
#          B = B//x
#          max *= x
#    return max

# def min(A,B):
#    min = (A*B)//max
#    return min

# print(max(A,B))
# print(min(A,B))
