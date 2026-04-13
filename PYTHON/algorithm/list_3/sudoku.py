import sys
sys.stdin = open("input_sudoku.txt","r")

T = int(input())
for t in range(T):
    arr = [list(map(int,input().split())) for _ in range(9)]
    result = 1

    correct = list(range(1,10))

    # 박스형 검색할 시작 point
    pnts = []
    for i in range(0,7,3):
        for j in range(0,7,3):
            pnts.append((i,j))

    # 가로줄 먼저
    for i in range(9):
        if sorted(arr[i]) != correct:
            result = 0
            break

        col = []
        for j in range(9):
            col.append(arr[j][i])
        if sorted(col) != correct:
            result = 0
            break

    # 박스형
    for x,y in pnts:
        data = []
        for i in range(3):
            for j in range(3):
                data.append(arr[x+i][y+j])
        if sorted(data) != correct:
            result = 0
            break

    print(f"#{t+1} {result}")