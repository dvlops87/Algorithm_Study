#1978 소수찾기 

count = int(input())

lis = list(map(int, input().split(" ")))

for i in lis:
    if i == 1 : lis[lis.index(i)] = 0 
    for x in range(2,i):
        if i%x == 0:
            lis[lis.index(i)] = 0 
            if i not in lis: break 


for x in lis :
    if x == 0 : 
        lis.remove(x)

print(len(lis))
