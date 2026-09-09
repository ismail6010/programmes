n=int(input());
for i in range(n//2,n+1,2): print(' '*(n-i)+'*'*i+' '*(n-i)+'*'*i)
for i in range(n,0,-2): print(' '*(n-i)+'*'*i+' '*(n-i)+'*'*i)
