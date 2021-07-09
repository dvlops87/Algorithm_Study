# 2581. 소수

# lis = [] 

# sum = 0 

# for x in range(int(input()), int(input())+1):
#     remain = []
#     for y in range(1,x+1):
#         if x % y == 0 :
#             remain.append(y)
    
#     if len(remain) == 2: lis.append(x)

# if len(lis) !=0:
#     for x in lis: 
#         sum += x
#     print(sum)
#     print(min(lis))  

# else : print(-1)

#에라토스테네스 체를 활용해서 진행

def prime_number(N,M):
    lis = [False,False]+[True for i in range(2,M+1)]
    big = int(M** 0.5) # M 의 최대 약수는 sqrt(n)임 따라서 sqrt(n) 까지 검사 
    for x in range(2, big+1):
        if lis[x] == True:
            for y in range(x+x , M+1, x) : 
                lis[y] = False


    return [x for x in range(N,M+1) if lis[x]== True]


N = int(input())
M = int(input())


result = prime_number(N, M)

if len(result) !=0:
    sum = 0 
    for r in result: 
        sum += r
    print(sum)
    print(min(prime_number(N, M)))

else : print(-1)
