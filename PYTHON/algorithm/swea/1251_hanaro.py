import sys
sys.stdin = open("input/1251_input.txt","r")


import heapq
def findboss(node):
    # global boss
    if boss[node] == node :
        return node
    boss[node] = findboss(boss[node])
    return boss[node]

def dist(n,xlst, ylst):
    q = []
    for i in range(n):
        for j in range(i+1,n):
            lgt = (xlst[i] - xlst[j])**2 + (ylst[i] - ylst[j])**2
            heapq.heappush(q,(lgt,i,j))

    ans = 0 # 합계
    cnt = 0 # line 개수
    while q:
        if cnt == n-1 : break
        cost, x,y = heapq.heappop(q)
        fx = findboss(x)
        fy = findboss(y)
        if fx == fy: continue
        else:
            ans += cost
            cnt += 1
            boss[fx] = fy
    return ans
T = int(input())
for tc in range(1,1+T):
    n = int(input())
    xlst = list(map(int,input().split()))
    ylst = list(map(int,input().split()))
    e= float(input())
    boss = list(range(n + 1))
    ans = dist(n,xlst,ylst)
    result = round(ans*e)
    print(f"#{tc} {result}")