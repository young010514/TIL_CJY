import sys
sys.stdin =open("input_nodeline.txt","r")

T = int(input())
for tc in range(1,T+1):
    v,e = map(int,input().split())
    lst = [list(map(int,input().split())) for _ in range(e)]
    s,g = map(int,input().split())
    nodes = list(range(1,v+1))
    # 사이클 방지를 위한 used 리스트
    used =[0] * (v+1)
    # 결과 담을 result
    result = 0
    def dfs(now,length):
        global  result
        for i in range(e):
            if lst[i].count(now):

                d = lst[i][1-lst[i].index(now)]

                if d == g :
                    result = length+1
                    return
                if used[d] ==0:
                    used[d] =1
                    dfs(d,length+1)
                    used[d] =0
    used[s] = 1
    dfs(s,0)
    print(f"#{tc} {result}")