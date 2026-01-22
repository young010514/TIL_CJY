arr = []
input_num= list(map(int,input().split()))

for index,num in enumerate(input_num):
    arr.append([])
    for i in range(4):
        arr[index].append(num+i)
for inner in arr:
    [print(x, end=' ') for x in inner]
    print()