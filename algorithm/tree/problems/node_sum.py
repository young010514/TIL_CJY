import sys
sys.stdin = open("input_nodesum.txt","r")

T= int(input())
for tc in range(1,T+1):
    n,m,l = map(int,input().split())
    leaf = [list(map(int,input().split())) for _ in range(m)]

    data = [0] * (n+5)
    for i in leaf:
        data[i[0]] = i[1]
    def dfs(now):
        if now * 2 > n :
            return data[now]
        left = 2*now
        right = 2*now +1
        return dfs(left) + dfs(right)
    result= dfs(l)

    print(f"#{tc} { result}")