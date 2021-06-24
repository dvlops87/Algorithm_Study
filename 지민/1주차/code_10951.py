# A+B -4

import sys 

while True:
   A, B = map(int, sys.stdin.readline().split(" "))
   if A == "\n" :
      break 
   print(A+B)
   