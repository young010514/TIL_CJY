n = int(input())
m = int(input())
# lines = [[] for _ in range(n+1)]
#
# for _ in range(m):
#     a,b,c = map(int,input().split())
lines = [list(map(int,input().split())) for _ in range(m)]
lines.sort(key=lambda x : x[2])
boss =[0] * (n+1)
def findboss(node):
    if boss[node] == 0 :
        return node
    boss[node] = findboss(boss[node])
    return boss[node]
def union(a,b):
    fa = findboss(a)
    fb = findboss(b)
    if fa == fb :
        return 0
    else:
        boss[fa] = fb
        return 1
ans = 0
cnt = 0
for a,b,cost in lines:
    if cnt == n-1 :
        break
    ret = union(a,b)
    if ret == 1:
        cnt += 1
        ans += cost
print(ans)