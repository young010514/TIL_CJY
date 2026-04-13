arr = []
n = input().split()
for i in n:
    arr.append(i)
big, small = [],[]

for x in arr :
    if x.isupper():
        big.append(x)
    else:small.append(x)
print(f'big={"".join(big)}')
print(f'small={"".join(small)}')
