n=int(input()); p=len(str(abs(n))); print('Armstrong' if n==sum(int(x)**p for x in str(abs(n))) else 'Not Armstrong')
