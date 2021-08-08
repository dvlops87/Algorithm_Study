N = int(input())
for i in range(N-1):
    print(' '*i,'*'*(2*(N-i)-1),' '*i,sep='')
for i in range(N):
    print(' '*(N-i-1),'*'*(2*i+1),' '*(N-i-1),sep='')