while True:
    try:
        A, B = map(int, input().split())
        print(A+B)
    except:
        break           # 더이상 입력이 없을 시 종료