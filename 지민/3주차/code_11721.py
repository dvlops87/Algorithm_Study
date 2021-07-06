# 11721 열 개씩 끊어 출력하기 

string = input()

result = ''
for x in range(len(string)):
    if (x+1)%10 == 0 and (x+1)!=0:
        print(string[x], end='\n' ) 
    else: print(string[x],end='')