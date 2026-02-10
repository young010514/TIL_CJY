

lst = [list(map(int,input().split())) for _ in range(5)]
check = [[0] * 5 for _ in range(5)]

call = []
for _ in range(5):
    call += list(map(int,input().split()))

bingo = 0
idx = 0
while bingo < 3:
    i = call[idx]
    for x,inner in enumerate(lst):
        if i not in inner:continue
        check[x][inner.index(i)] = 1
    bingo = 0
    # 가로줄 확인
    for inner in check :
        if sum(inner) == 5 :bingo +=1

    for j in range(5):
        data = True
        for i in range(5):
            if check[i][j] == 0:
                data = False
                break
        if data :
            bingo += 1
    right, left = True, True
    for i in range(5):
        if check[i][i] == 0 : 
            right = False
        if check[i][4-i] == 0: 
            left = False
    bingo += (right + left)
    idx += 1
print(idx)