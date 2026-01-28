arr = list(map(int,input().split()))

for i in range(1,6):
    arr[i] += arr[i-1]
[print(x,end=' ') for x in arr]