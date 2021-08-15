#11005 진법 변환2 --> 복잡한 내 코드 
import sys

def convert(N, B):
    number = dict()
    ascii_code = 65
    result = str()

    # 진법 변환을 위한 딕셔너리 생성 
    for n in range(0,B):
        if n >=10:
                if n == 10:
                    number[str(n)] = chr(ascii_code)
                else:
                    ascii_code +=1 
                    number[str(n)] = chr(ascii_code)
        else: 
            number[str(n)] = str(n)

    
    while True:
        
        share = N//B
        print(share)
        result += number.get(str(share))
        # print(share)
        N = N//B
        remain = N%B

        if N < B: 
            result += number.get(str(N))
            result += number.get(str(remain))
            break
        else: 
            result += number.get(str(remain))
        

    return result[::-1]


N,B = map(int, sys.stdin.readline().split(" "))
print(convert(N, B))
