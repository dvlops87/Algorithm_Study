#다 더하고 빼기
nanList = []
total = 0
for i in range(9):
    nanList.append(int(input()))    #난쟁이 리스트에 추가
    total += int(nanList[i])        #난쟁이 키 총 합
total -= 100
nanList.sort()
for i in range(len(nanList)-1):
    for j in range(i+1,len(nanList)):
        if total==nanList[i]+nanList[j]:
            del nanList[j]
            del nanList[i]
            break
for i in range(len(nanList)):
    print(nanList[i])