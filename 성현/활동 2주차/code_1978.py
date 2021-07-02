T = int(input())
list = list(map(int,(input().split())))
count=0
out=0
for i in list:
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2:
        out+=1
    count=0
print(out)