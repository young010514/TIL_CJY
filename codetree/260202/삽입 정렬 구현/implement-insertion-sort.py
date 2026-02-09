n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
result = []
for i in range(len(arr)):
    result.append(arr[i])
    for j in range(i,0,-1):
        if result[j - 1] > result[j]:
            result[j-1], result[j] = result[j], result[j-1]
        else:break
print(*result)