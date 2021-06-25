#3460. 이진수
import sys

T = int(sys.stdin.readline())

for _ in range(T):
   n = int(sys.stdin.readline())
   new = str(bin(n)[2:])[::-1]

   count = 0 
   for x in new : 
      if int(x)==1:
         print(count, end= " ")
         count +=1 
      else: 
         count +=1 
         