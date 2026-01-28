arr = []
result = []
for i in range(4):
    arin = list(input())
    arr.append(arin)
    result.append(len(arr[i]))
for x in sorted(result):
    print(x,end=' ')