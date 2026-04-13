import sys
sys.stdin = open("input_swim.txt","r")

def dfs(now,cost):
    global  result
    if now >=11 :
        if cost < result :
            result = cost
        return
    nxt = now + 1
    if arr[nxt] == 0:
        dfs(nxt,cost)
    else:
        dfs(nxt, cost + d*arr[nxt]) # 1일권
        dfs(nxt, cost + m)    # 1개월
        dfs(nxt+2, cost + m3) # 3개월

T = int(input())
for tc in range(1,T+1):
    d,m,m3, y = map(int,input().split())
    arr = list(map(int,input().split()))

    result = y  # result 는 연간 cost 로 초기화
    for i in range(12):
        if arr[i] !=0 :
            dfs(i-1, 0)
            break
    print(f"#{tc} {result}")
