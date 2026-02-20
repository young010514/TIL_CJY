import sys
sys.stdin = open("input_miro1.txt","r")

for _ in range(10):
    tc = int(input())
    miro = [list(input()) for _ in range(16)]
    st,ed = 0,0
    for i in range(16):
        for j in range(16) :
            if miro[i][j] == "2" :
                st = (i,j)
                break
    for i in range(15,-1,-1):
        for j in range(15,-1,-1) :
            if miro[i][j] == "3" :
                ed = (i,j)
                break
    result = 0
    drs = [(-1,0),(1,0),(0,1),(0,-1)]
    def dfs(x,y):   # x,y좌표
        global result

        for i,j in drs:
            dx = x+i
            dy = y+j
            if dx <0 or dy< 0 or dx >15 or dy >15: continue
            if miro[dx][dy] == "0":

                miro[dx][dy] = "1"
                dfs(dx,dy)
                miro[dx][dy] = "0"
            if miro[dx][dy] == "3" :
                result = 1
                return
    dfs(st[0],st[1])
    print(f"#{tc} {result}")