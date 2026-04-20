n = int(input())
arr = []
for i in range(4):
    inner= []
    for j in range(4):
        inner.append(n + j + i*4)
    if i % 2 ==0 :
        arr.append(inner)
    else:arr.append(inner[::-1])
for inner in arr:
    [print(x,end=' ') for x in inner]
    print()