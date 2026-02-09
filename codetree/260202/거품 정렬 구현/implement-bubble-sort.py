n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
sorted = False
while sorted == False:
    sorted = True
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1] , arr[i]
            sorted=False
[print(x, end=' ') for x in arr]