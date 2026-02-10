import sys
sys.stdin = open("input_bingo.txt","r")


lst = [list(map(int,input().split())) for _ in range(5)]
check = [[0] * 5 for _ in range(5)]

call = []
for _ in range(5):
    call += list(map(int,input().split()))
bingo = 0

for idx, i in enumerate(call):
    if bingo == 3 :
        print(idx + 1)
        break
    bingo = 0
    for x,inner in enumerate(lst):
        if i not in inner:continue
        check[x][i.index(inner)] = 1

    # 가로줄 확인
    for inner in check :
        if sum(inner) == 5 :bingo +=1
    for j in range(5):
        data = 0
        for i in range(5):
            data += check