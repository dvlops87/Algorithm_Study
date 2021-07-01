# 11021. A+B - 7 합도 String으로 출력해야했다..

test = int(input())
for x in range(test):

    A,B = map(int, input().split(" "))
    print("Case #{}: {}".format(x+1 , A+B))