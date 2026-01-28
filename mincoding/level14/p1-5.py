arr = []
for i in range(3):
    arr1 = list(map(int,input().split()))
    arr.append(arr1)
sum_data =0
for x, inner in enumerate(arr):
    for y in inner[:x+1]:
        sum_data += y
print(sum_data)
