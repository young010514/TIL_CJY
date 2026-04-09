import sys
sys.stdin = open("input_8.txt","r")

dts = [(0,0),(-1,0),(0,1),(1,0),(0,-1)]  # 이동 정보


def addresult(ax, ay, bx, by):
    A = []
    B = []

    # 접근 가능한 BC 저장 (값 + 인덱스)
    for i in range(a):
        cy, cx, c, p = charge[i]

        if abs(ax - cx) + abs(ay - cy) <= c:
            A.append((p, i))
        if abs(bx - cx) + abs(by - cy) <= c:
            B.append((p, i))

    max_val = 0

    # 둘 다 못 쓰는 경우
    if not A and not B:
        return 0

    # 한쪽만 가능한 경우
    if not A:
        return max(p for p, _ in B)
    if not B:
        return max(p for p, _ in A)

    # 조합 비교 (핵심)
    for pa, ia in A:
        for pb, ib in B:
            if ia == ib:
                temp = pa
            else:
                temp = pa + pb
            max_val = max(max_val, temp)

    return max_val

def move(usera,userb):
    global ans
    ax,ay,bx,by = 1,1,10,10
    for i in range(m):
        ans += addresult(ax,ay,bx,by)
        howa = usera[i]
        howb = userb[i]
        dax,day = ax + dts[howa][0], ay + dts[howa][1]
        dbx,dby = bx + dts[howb][0], by + dts[howb][1]
        ax, ay, bx, by =dax,day,dbx,dby
    ans += addresult(ax,ay,bx,by)

T = int(input())
for tc in range(1,T+1):
    m,a = map(int,input().split())
    usera = list(map(int,input().split()))
    userb = list(map(int,input().split()))
    charge = [list(map(int,input().split())) for _ in range(a)]
    ans = 0
    move(usera,userb)

    print(f"#{tc} {ans}")