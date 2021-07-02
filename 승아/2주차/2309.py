list = [int(input()) for i in range(9)]
total = sum(list)

for i in range(9):
    for j in range(i+1,9):
        if total - (list[i] + list[j]) == 100:
            num1,num2=list[i],list[j]

            list.remove(num1)
            list.remove(num2)
            list.sort() # 오름차순 정리

            for i in range(len(list)):
               print(list[i])
            break

    if len(list)<9:
        break


# combination 라이브러리 사용하기 -> 오답...

# from itertools import combinations
#
# height = [int(input()) for i in range(9)]
# total = sum(height)
#
# a = list((combinations(height, 2)))
#
# for i in a:
#     if total - sum(i) == 100:
#         height.remove(i[0])
#         height.remove(i[1])
#         height.sort()
#         for j in height:
#             print(j)
#         break




# combination 구현하기
# height = [int(input()) for i in range(9)]

# print(a)

# print(list(combinations(a,1)))

# if a == 100:
#     print(a)
#
# a = list(combinations(height, 7))
# print(a)

# if sum(a) == 100:
#     print(a)
# height.append(input())

# lists = [1, 2, 3]
# a = list(combinations(lists, 2))
# print(list(a))
