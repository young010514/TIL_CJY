arr = [3,4,2,5,7,9]
a, b = map(int, input().split())
arr[b], arr[a] = arr[a], arr[b]
[print(i, end=' ') for i in arr]