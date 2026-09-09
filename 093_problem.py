n=int(input());
for i in range(1,n+1): print(' '*(n-i)+' '.join(map(str,range(1,2*i))))
