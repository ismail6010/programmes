nums=[]
while True:
    n=float(input())
    if n==-1: break
    nums.append(n)
print(len(nums), sum(nums)/len(nums) if nums else 0)
