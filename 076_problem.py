def count(s):
    return 0 if not s else (s[0].lower() in 'aeiou')+count(s[1:])
print(count(input()))
