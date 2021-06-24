trainNum = [0 for i in range(10)]
for num in range(10):
    i,o = map(int,(input().split(' ')))
    if num ==0:                                 #첫번째 경우에만 특별히 적용. 사람들이 안탔기 때문
        trainNum[0] = -i+o
    else : 
        trainNum[num] = trainNum[num-1]-i+o
trainNum.sort()
print(trainNum[9])
