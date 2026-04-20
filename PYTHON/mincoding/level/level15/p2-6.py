arr = [0,0,0,0,0,0,0,0,0]
for i in range(3):
    a,b= map(int,input().split())
    for idx in range(a,b+1):
        arr[idx] += 1
[print(x, end=' ') for x in arr]