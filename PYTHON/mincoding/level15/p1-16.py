a = input()
arr = [[],[],[]]
ord_now = ord(a)
for x in range(-1,-4,-1):
    for y in range(-x):
        arr[x].append(chr(ord_now))
        ord_now += 1
for inner in arr:
    [print(x,end='') for x in inner]
    print()