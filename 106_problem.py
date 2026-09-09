n=int(input());
for i in range(n): print('* '*(n//2) if i in [0,n-1] else ' '*(n//2)+'*')
