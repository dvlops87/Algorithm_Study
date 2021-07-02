import sys
T = int(input())
data = []
for i in range(T):
    data=(list(map(int,sys.stdin.readline().split())))
    data.sort()
    print(data[-3])
