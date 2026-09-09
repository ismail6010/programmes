n=int(input()); seen=set()
while n!=1 and n not in seen:
    seen.add(n); n=sum(int(x)**2 for x in str(n))
print('Happy' if n==1 else 'Not Happy')
