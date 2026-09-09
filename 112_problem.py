n=int(input());
for i in range(n): print(''.join('*' if i in [0,n-1] or j in [0,n-1] or i==j or i+j==n-1 else ' ' for j in range(n)))
