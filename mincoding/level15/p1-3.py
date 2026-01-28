arr = list(map(int,input().split()))
for i in range(len(arr)-1):
    result = True
    if abs(arr[i] - arr[i+1]) >= 3:
        result = False
if result : print("완벽한배치")
else :print("재배치필요")