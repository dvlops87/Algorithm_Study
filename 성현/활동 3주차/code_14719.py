import sys
input = sys.stdin.readline

maxH = 1
maxL = 0

H, W = map(int, input().strip().split())

pillar = list(map(int, input().strip().split()))
for i in range(len(pillar)):
    if maxH < pillar[i]:
        maxH = pillar[i]
        maxIndex = i

total = 0
temp = 0
for i in range(maxIndex +1):
    if pillar[i] > temp:
        temp = pillar[i]
    total += temp
temp=0
for i in range(W -1, maxIndex, -1):
    if pillar[i] > temp:
        temp=pillar[i]
    total += temp
print(total - sum(pillar))