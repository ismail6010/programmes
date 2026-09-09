n=int(input());
for i in range(n,0,-1): print(' '.join(chr(65+j) for j in range(i)))
