# 11719 그대로 출력하기


while True:
    try : 
        x = input()
    except EOFError:
        break
    print(x)