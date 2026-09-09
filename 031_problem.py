m=int(input());
if m==2: print(29 if int(input())%4==0 else 28)
elif m in [4,6,9,11]: print(30)
else: print(31)
