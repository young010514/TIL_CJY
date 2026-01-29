arr = list(range(1,10))
ip = []
for i in range(3):
    ip.append(list(map(int,input().split())))
for inner in ip:
    for x in inner:
        if x in arr: arr.pop(arr.index(x))
[print(x,end=' ') for x in arr]