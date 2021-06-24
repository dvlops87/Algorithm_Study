N = int(input())
numList = map(int,input().split(' '))
numList = list(numList)
numList.sort()                          #오름차순으로 정렬
bigNum = numList[len(numList)-1]
smallNum = numList[0]
print(smallNum, bigNum)