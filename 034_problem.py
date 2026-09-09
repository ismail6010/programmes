import math
a=float(input()); b=float(input()); c=float(input()); d=b*b-4*a*c
if d>0: print((-b+math.sqrt(d))/(2*a),(-b-math.sqrt(d))/(2*a))
elif d==0: print(-b/(2*a))
else: print('Imaginary')
