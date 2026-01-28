arr1 = []
for i in range(5):
    arr = list(map(int,input().split()))
    arr1.append(arr)

for i in arr1:
    print(sum(i),end=' ' )