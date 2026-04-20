import sys
sys.stdin = open("input/input_robot.txt","r")

dts = [(0,1),(-1,0),(0,-1),(1,0)]*2  # 보고있는 방향 기준에서 반시계방향으로 탐색할 예쩡
def robot(x,y):
    days =[[-1] * n for _ in range(n)]
    ans = 0
    days[x][y] =0
    for d in range(4):
        now_ans = 0
        q = [(x,y,0,0,d)]  # now x, now y, count, 지금 보고 있는 방향 index
        for now in range(1,m):  # m번 돌면 됨
            if not q:  # 더이상 이동하지 못하는 경우
                break
            nx,ny,time,cnt,nowd = q.pop()
            now_ans = cnt
            for i,j in dts[d+1:d+5]:
                dx = nx+i
                dy = ny+j
                if 0<= dx <n and 0<= dy<n:
                    if arr[dx][dy] ==1: continue
                    if days[dx][dy] == -1 :
                        days[dx][dy] = now
                        q.append((dx,dy,now,cnt))
                        continue
                    if now - days[dx][dy] <5: continue
                    days[dx][dy] = -1
                    q.append((dx,dy,-1))
                        break
        ans = max(now_ans,ans)

    return ans

T = int(input())
for tc in range(1,T+1):
    n,m = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1: continue
            robot(i,j)
