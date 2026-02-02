n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

for i in range(len(arr)):
    min_data = arr[i]
    idx = i
    for j in range(i, len(arr)):
        if arr[j] < min_data:
            idx = j
            min_data = arr[j]
    arr[i], arr[idx] = min_data, arr[i]
[print(x, end=' ') for x in arr]