r=int(input()); c=int(input());
for i in range(r): print('*'*c if i in [0,r-1] else '*'+' '*(c-2)+'*')
