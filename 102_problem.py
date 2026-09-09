n=int(input());
for i in range(n):
    s=list(range(i+1))+list(range(i-1,-1,-1)); print(' '*(n-i-1)+' '.join(chr(65+j) for j in s))
