n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(m)]
arr.sort(key=lambda x : x[2], reverse=True)

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
        boss[fb] = fa
        return 1

cnt,ans = 0,0
while arr:
    if cnt >= n-2 :
        break
    a,b,c = arr.pop()
    ret = union(a,b)
    if ret :
        ans += c
        cnt +=1
    else: continue
print(ans)