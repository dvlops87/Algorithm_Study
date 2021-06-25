#10870 피보나치 수 5

def fibo(n):
   result = {}
   for x in range(n+1):
      if x ==0:
         result[0] = 0 
      elif x ==1:
         result[1] = 1
      else:
         result[x] = result[x-1] + result[x-2]
      
   return result.get(n) #맨 마지막 값 가지고 오기 


print(fibo(int(input())))