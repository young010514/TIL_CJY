import sys
sys.stdin = open("input_mintree.txt","r")

def findx(m):
    global members
    if members[m] == "" : return m
    ret = findx(members[m])
    members[m] = ret
    return ret

def union(a,b,c):
    global result
    fa = findx(a)
    fb = findx(b)
    if fa == fb : return
    result += c
    if rank[fa] > rank[fb] :
        members[fb] = fa
    elif rank[fa] < rank[fb]:
        members[fb] =fa
    else:
        members[fb] =fa
        rank[fa] += 1

T = int(input())
for tc in range(1,T+1):
    v,e = map(int,input().split())
    lines = [list(map(int,input().split())) for _ in range(e)]
    # 가중치를 기준으로 sort
    lines.sort(key=lambda x : x[2])
    members = [""] * (v+1)
    rank = [0] * (v+1)
    result= 0
    for x in lines:
        union(x[0],x[1],x[2])
    print(f"#{tc} {result}")