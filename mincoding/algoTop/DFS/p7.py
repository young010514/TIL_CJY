n,m = map(int,input().split())
nlst= [tuple(map(int,input().split())) for _ in range(n)]

arr = [0] * (n+1)
rank = [0] * (n+1)

def findb(x):
    if arr[x] == 0 :
        return x
    ret =  findb(arr[x])
    arr[x] = ret
    return ret

def union(a,b):
    global arr
    fa = findb(a)
    fb = findb(b)
    if fa == fb : return
    # arr[fb] = fa
    # 작은게 밑으로 들어가게 최적화
    if rank[fb] > rank[fa] :
        arr[fa] = fb
    elif rank[fb] < rank[fa] :
        arr[fb] = fa
    else:
        arr[fb] = fa
        rank[fa] += 1

def round1(x):
    roundlst = [nlst[x-1]]
    for i in range(1,1+n):
        if arr[i] == x:
            roundlst.append((nlst[i-1]))
    # print(roundlst)
    result = 0
    prev = roundlst[-1]
    for d in range(len(roundlst)):
        next = roundlst[d]
        result += abs(prev[0]-next[0]) + abs(prev[1]-next[1])
        prev=roundlst[d]
    return result

for _ in range(m):
    a,b = map(int,input().split())
    union(a,b)
# print(arr)
Min = 3e16
for i in range(1,n+1):
    if arr[i]==0:
        if arr.count(i) > 0 :
            result = round1(i)
            if result < Min :
                Min = result
print(Min)
