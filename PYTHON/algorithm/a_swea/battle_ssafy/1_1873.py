import sys
sys.stdin = open("input_1.txt","r")

T = int(input())
def move(how):  # 현재 좌표 x,y,어떻게 움직일지 how
    global nx, ny
    forshoot = {"<": (0, -1), ">": (0, 1), "v": (1, 0), "^": (-1, 0)}
    if how == "U":
        # 이동하지 못하는 경우를 대비해서 우선 방향 변경
        arr[nx][ny] = "^"
        # 이동 가능한 경우
        if 0 <= nx - 1 < h:
            if arr[nx - 1][ny] == ".":
                arr[nx][ny] = "."
                arr[nx - 1][ny] = "^"
                nx -= 1  # 현재 좌표 변경
    elif how == "D":
        arr[nx][ny] = "v"
        if 0 <= nx + 1 < h:
            if arr[nx + 1][ny] == ".":
                arr[nx][ny] = "."
                arr[nx + 1][ny] = "v"
                nx += 1
    elif how == "L":
        arr[nx][ny] = "<"
        if 0 <= ny - 1 < w:
            if arr[nx][ny - 1] == ".":
                arr[nx][ny] = "."
                arr[nx][ny - 1] = "<"
                ny -= 1
    elif how == "R":
        arr[nx][ny] = ">"
        if 0 <= ny + 1 < w:
            if arr[nx][ny + 1] == ".":
                arr[nx][ny] = "."
                arr[nx][ny + 1] = ">"
                ny += 1

    elif how == "S":

        stingx, stingy = nx, ny
        gapx, gapy = forshoot[arr[nx][ny]]
        while 1:
            dx = stingx + gapx
            dy = stingy + gapy

            if dx < 0 or dy < 0 or dx > h - 1 or dy > w - 1:  # 범위 밖으로 나가는 경우
                break
            if arr[dx][dy] == "#": break  # 강철로 만들어진 경우
            if arr[dx][dy] == "*":
                arr[dx][dy] = "."
                break

            stingx, stingy = dx, dy  # 한번 더 전진


for tc in range(1,T+1):
    h,w = map(int,input().split())
    arr = [list(input()) for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if arr[i][j] in ["v","<",">","^"] :
                nx,ny = i,j
                break

    n = int(input())
    lst = list(input())
    for how in lst:
        move(how)
    print(f"#{tc}", end=' ')
    for i in range(h):
        print("".join(arr[i]))
