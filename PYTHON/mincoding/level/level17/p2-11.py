arr = [3,5,4,2]
bit = list(map(int,input().split()))
result =0
for x in range(len(bit)):
    if bit[x] :
        result += arr[x]
print(result)