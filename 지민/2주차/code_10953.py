# 10953. A+B -6 

case = int(input())

for _ in range(case):
    try:
        A,B = map(int, input().split(","))
    except:
        print("Try again")
        break 
    
    print(A+B)