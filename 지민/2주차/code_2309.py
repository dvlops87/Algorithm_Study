# 2309. 일곱 난쟁이

from itertools import permutations,combinations

items = [] 
for _ in range(9):
   height = int(input())
   items.append(height)

comb = (list(combinations(items,7)))
for x in comb:
   if sum(x)==100:
      answer = sorted(x)
      
for x in answer:
   print(x)