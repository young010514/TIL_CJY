arr = [input().strip() for _ in range(3)]
max_len = 0
idx = 0
for i, st in enumerate(arr):
    if len(st) >= max_len:
        idx = i
        max_len = len(st)

arr[0], arr[idx] = arr[idx], arr[0]
[print(i) for i in arr]