import sys
sys.stdin = open("input_hanaro.txt","r")

def findboss(m):
    if arr[m] == 0 : return m
    ret = findboss(arr[m])
    arr[m] = ret
    return ret
def union(a,b,d):
    global cnt, result
    fa = findboss(a)
    fb = findboss(b)
    if fa == fb : return
    if rank[fa] > rank[fb] :
        arr[fb] = fa
    elif rank[fa] < rank[fb]:
        arr[fa] = fb
    else:
        rank[fb] += 1
        arr[fa] = fb
    cnt += 1
    result += d

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    xlst = list(map(int,input().split()))
    ylst = list(map(int,input().split()))
    e = float(input())
    lines = []
    for i in range(n):
        for j in range(i+1,n):
            data = (xlst[i] - xlst[j]) ** 2 + (ylst[i] - ylst[j]) ** 2
            lines.append((i,j,data))
    lines.sort(key=lambda x : x[2])

    result, cnt = 0,0

    rank = [0] * n
    arr = [0] * n

    for x,y,d in lines:
        union(x,y,d)
        if cnt == n-1 : break
    print(f"#{tc} {e*result:.0f}")