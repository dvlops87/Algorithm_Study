# n = int(input())
# num = list(map(int, input().split()))
# so = 0
#
# for i in num:
#     so = 0;
#     if (i ==1):
#         continue
#     for j in range(2, i+1):
#         if(i%j==0):
#             so+=1
#         if(so == 1):
#             so += 1
# print(so)

n = int(input())
num = map(int, input().split())
so = 0
for i in num:
    error = 0
    if i > 1 :
        for j in range(2, i):
            if i % j == 0:
                error += 1
        if error == 0:
            so += 1
print(so)
