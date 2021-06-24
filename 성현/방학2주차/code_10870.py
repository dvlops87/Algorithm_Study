n = int(input())
fNum = [0 for i in range(n+1)] #입력 받은 n+1만큼 리스트 생성. 왜 n+1이냐? 피보나치는 0번째 피보나치 숫자가 존재하기 때문
for i in range(n+1):
    if i == 1:
        fNum[i]=1
    elif i > 1:
        fNum[i] = fNum[i-1]+fNum[i-2]
print(fNum[n])