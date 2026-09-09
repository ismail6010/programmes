n=int(input());
for i in range(1,n+1): print(' '.join(str(j%2) for j in range(1,i+1)))
