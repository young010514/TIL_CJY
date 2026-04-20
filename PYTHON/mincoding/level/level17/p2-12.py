arr = []
for i in range(5):
    arr.append([])
    for j in range(5):
        arr[i].append(chr(ord("A") + i*5 + j))
s = input()
for i,inner in enumerate(arr):
    for j, x in enumerate(inner):
        if s == x :
            print(f"{i-2},{j-2}")