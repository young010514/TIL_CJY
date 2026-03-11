import sys
sys.stdin = open("input_minpath.txt","r")

T = int(input())
for tc in range(1,T+1):
    n,m = map(int,input().split())
    lines= [list(map(int,input().split())) for _ in range(m)]
    lines.sort(key=lambda x : (x[0],x[2]))
    # print(lines)
    result = 2e10
    def dfs(x,Sum) :
        global result
        if Sum > result : return
        if x == n:
            if result > Sum :
                result = Sum
            return
        for inner in lines:
            if inner[0] < x : continue
            if inner[0] > x : break
            dfs(inner[1], Sum + inner[2])


    for inner in lines:
        if inner[0] != 0 : break
        dfs(inner[1],inner[2])  # 현재 좌표, Sum
    print(f"#{tc} {result}")