# 11718. 그대로 출력하기

while True:
    try: 
        sentence = input()
        if sentence == '': break
    except EOFError:
        break
    print(sentence)