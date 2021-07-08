x = int(input())
y = int(input())
prime_number = list(range (3,y+1,2))
prime_number.insert(0,2)
final_list = []
for i in range(3,y+1,2):
    if i in prime_number:
        for j in range(i+i, y+1, i):
            if j in prime_number:
                prime_number.remove(j)
for k in prime_number:
    if k >= x and k <= y:
        final_list.append(k)
if len(final_list) > 0:
    print(sum(final_list))
    print(final_list[0])
else:
    print('-1')