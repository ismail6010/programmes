n=int(input());
for i in range(1,n+1): print('*'*i if i in [1,n] else '*'+' '*(i-2)+'*')
