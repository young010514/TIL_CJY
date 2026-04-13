lst = list(input())
arr = [list(map(int,input().split())) for _ in range(8)]
print(arr)
for j in range(8):
    data = 0
    for i in range(8):
        if arr[i][j] == 1: data += 1
    if data ==0:
        root = j
        break

path = []
def abc(idx):
    global path
    path.append(idx)
    if sum(arr[idx]) ==0 :
        return

    for i in range(8):
        if arr[idx][i] == 1:
            abc(i)
            # path.pop()
abc(root)
for i in path:
    print(lst[i],end='')