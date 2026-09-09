n=int(input());
for i in range(n): print(' '.join(str(__import__('math').comb(i,j)) for j in range(i+1)))
