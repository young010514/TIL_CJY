com = int(input())
n = int(input())
lst = [tuple(map(int,input().split())) for _ in range(n)]
virus = [0]*(com+1)
virus[1] = 1
def dfs(now):
    for i,j in lst:
        if i != now and j != now  :continue
        if i == now and virus[j] ==0 :
            virus[j] =1
            dfs(j)
        elif j == now and virus[i] == 0:
            virus[i] =1
            dfs(i)
dfs(1)
print(sum(virus) - 1)