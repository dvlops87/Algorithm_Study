N = input() 

modi_N = len(N)%3 

if modi_N == 1:
	N = ''.join(reversed("00"+N))
	
elif modi_N ==2 : 	
	N = ''.join(reversed("0"+N))



result = str()

for x in range(1, len(N)+1):
	if x%3 == 0 :
		result += str(int(N[x-1]) *(2**2))
	elif x%3 == 1 :
		result += str(int(N[x-1])*1)
	elif x%3 == 2 : 
		result += str(int(N[x-1])* (2**1))

resu = int()
res = str() 

for x in range(1, len(result)+1):
	resu += int(result[x-1])
	if x %3 ==0:
		res += str(resu)
		resu =0 

print(''.join(reversed(res)))
	
	
	
