import sys

v, e = map(int, sys.stdin.readline().split())
arr = []
for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    arr.append((c,a,b))

# 크루스칼 알고리즘은 정렬이 필요!
arr.sort(key=lambda x: x[0])
parent = list(range(v + 1))

#유니온 파인드 연산
def union(a, b):
    a = find(a)
    b = find(b)

    if b < a:
        parent[a] = b
    else:
        parent[b] = a
def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])  # 경로 압축
    return parent[a]

sum = 0
for c, a, b in arr:
    if find(a) != find(b):
        union(a, b)
        sum += c

print(sum)
