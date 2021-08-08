import sys 


system = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ" #10진법이면 9 까지, 36진법이면 Z까지 표현된다
N, B = map(int, sys.stdin.readline().split())
answer = ''

while N != 0:
    answer += str(system[N % B]) 
    N //= B
    
print(answer[::-1])