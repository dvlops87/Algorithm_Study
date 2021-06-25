#2460 지능형 기차 2

people = 0
result = []

for _ in range(10):
   minus , plus = map(int, input().split(" "))

   people = people+plus-minus
   result.append(people)

print(max(result))