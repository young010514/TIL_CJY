import sys
sys.stdin= open("input/in_2105.txt","r")

def dfs(r,c,d,visited):
    global max_des, stx,sty

    if d == 3 and r == stx and c ==sty:
        if len(visited) > max_des:
            max_des = len(visited)
        return

    if r<0 or c <0 or r > n-1 or c > n-1 or (arr[r][c] in visited):return

    visited.append(arr[r][c])

    dfs(r+dts[d][0], c + dts[d][1], d, visited)
    if d < 3 :
        dfs(r+dts[d+1][0], c+dts[d+1][1], d+1, visited)
    visited.pop()

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    dts = [(1,-1),(1,1),(-1,1),(-1,-1)]  # 반시계 방향으로 회전
    # 답을 -1로 초기화
    max_des = -1

    for i in range(n-2):
        for j in range(1,n-1):
            stx, sty= i,j # 시작 지점을 사각형 위쪽으로 잡기
            dfs(i,j,0,[])

    print(f"#{tc} {max_des}")
