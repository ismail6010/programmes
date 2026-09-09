def check(s):
    return True if len(s)<2 else s[0]==s[-1] and check(s[1:-1])
s=input(); print('Palindrome' if check(s) else 'Not Palindrome')
