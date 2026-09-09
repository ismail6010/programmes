n=int(input());
for i in range(n): print('*'+' '*(2*i-1)+'*' if i not in [0,n-1] else '*')
for i in range(n-2,-1,-1): print('*'+' '*(2*i-1)+'*' if i else '*')
