#1978 소수찾기 

num = int(input())
lis = list(map(int,input().split(" ")))


count = 0

for x in lis:
    if x!=1:
        share = []
        for y in range(1,x+1):
            if x%y ==0:
               share.append(y)
        if len(share) == 2:
            count+=1

print(count)



# count = int(input())

# lis = list(map(int, input().split(" ")))

# for i in lis:
#     if i == 1 : lis[lis.index(i)] = 0 
#     for x in range(2,i):
#         if i%x == 0:
#             lis[lis.index(i)] = 0 
#             if i not in lis: break 


# for x in lis :
#     if x == 0 : 
#         lis.remove(x)

# print(len(lis))