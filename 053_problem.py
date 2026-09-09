def product(n):
    return n if n<10 else n%10*product(n//10)
print(product(abs(int(input()))))
