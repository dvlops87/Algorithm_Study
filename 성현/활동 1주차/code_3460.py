T = int(input())
nList = []                              #이진수 계산 시 나눌 숫자 저장
numList = []                            #이진수 계산 후 나온 이진수 저장
locate=0                                #이진수의 위치 저장
for i in range(T):
    n = int(input())                    #T개의 숫자 중 i번째로 계산할 숫자 입력 받음
    nList.append(n)
    n=nList[i]
    while(True):
        if (n%2)==1:
            numList.append(locate)      #1이 남으면 == 소인수 분해 계산 시 1이 남는 상황
        if n==1:
            break
        n=n//2                          #소숫점으로 나오지 않게 /2개를 써서 자연수로만 계산하게끔 설정
        locate+=1
    print(" ".join(map(str,numList)))   #join 내장 함수를 통해 numList를 공백으로 이은 후 출력
    numList.clear()
    locate=0