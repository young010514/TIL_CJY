v,e = map(int,input().split())
lines = [list(map(int,input().split())) for _ in range(e)]
lines.sort(key=lambda x : x[2])

boss =list(range(v+1))
rank = [0] * (v+1)
def findboss(node):
    if boss[node] == node:
        return node
    boss[node] = findboss(boss[node])
    return boss[node]
def union(a,b):
    fa = findboss(a)
    fb = findboss(b)
    if fa == fb : return False
    if rank[fa] < rank[fb]:
        boss[fa] = fb
    elif rank[fa] > rank[fb]:
        boss[fb] = fa
    else:
        boss[fb] = fa
        rank[fa] += 1
    return True

result =0
cnt =0
for st,ed,w in lines:
    cost = union(st,ed)
    if cost :
        cnt += 1
        result += w
    if cnt == v-1 : break
print(result)
