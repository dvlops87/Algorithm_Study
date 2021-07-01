#11022. A+B -8 

for x in range(int(input())): 
    A,B = map(int, input().split(" "))
    print("Case #{}: {} + {} = {}".format(x+1,A,B,A+B))