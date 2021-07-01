# 2693. N번째 큰 수

import sys

test = int(sys.stdin.readline())

for _ in range(test):
    arr = sorted(list(map(int, sys.stdin.readline().split(" "))))
    del arr[len(arr)-1]
    del arr[len(arr)-1]
    print(max(arr))