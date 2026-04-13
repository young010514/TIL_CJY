n = int(input())
arr = []
for _ in range(n):
    lst = input().split()
    if lst[0] == "push":
        arr.append(lst[1])
    elif lst[0] == 'top':
        if arr :print(arr[-1])
        else:print(-1)
    elif lst[0] == "size":
        print(len(arr))
    elif lst[0] == "empty":
        if arr :print(0)
        else:print(1)
    elif lst[0] == "pop":
        if len(arr) == 0: print(-1)
        else:print(arr.pop())
