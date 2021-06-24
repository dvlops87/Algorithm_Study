T=int(input())
list = [0] * T
for i in range(T):
    numbers = input().split(' ')
    list[i] = int(numbers[0])+int(numbers[1])
for i in range(len(list)) :
    print(list[i])