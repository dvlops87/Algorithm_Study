N = input() 

modi_N = len(N)%3 

if modi_N == 1:
	N = "00"+N
	
elif modi_N ==2 : 	
	N = "0"+N
	
result = str()

for n in range(len(N)):
	if n % 3 ==1 : 
		n  = n*(2**1) 
	elif n % 3 == 2:
		n = n*(2**2)
	else:
		n = n*(2**3)
	
	
	
