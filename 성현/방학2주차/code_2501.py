N, K = map(int, input().split(' '))
numList = [0]*N                     #N개 만큼 리스트 생성
j=0
for i in range(1,N+1):
    if (N%i)==0:
        numList[j]=i                #나머지가 0이면 약수로 판단하고 리스트에 넣는다
        j+=1

if len(numList) !=0:
    print(numList[K-1])             #약수가 1개라도 있으면 출력
else :
    print(0)
