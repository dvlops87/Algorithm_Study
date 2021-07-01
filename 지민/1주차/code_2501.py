# 2501. 약수 구하기 

N,K = map(int,input().split(" "))
answer  = [] 

for n in range(1,N+1):
   if N%n == 0 :
      answer.append(n)


if K > len(answer): 
   print(0)
else: print(answer[K-1])