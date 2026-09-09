n=int(input()); x=1
for i in range(1,n+1):
    print(' '.join(str(x+j) for j in range(i))); x+=i
