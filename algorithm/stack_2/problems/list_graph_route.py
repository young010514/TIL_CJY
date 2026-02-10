import  sys
sys.stdin = open("input_route.txt", "r")

T = int(input())
for tc in range(1,T+1):
    v,e = map(int,input().split())
    lst1 = [[] for _ in range(v+1)]

    for _ in range(e):
        a,b = map(int,input().split())
        lst1[a].append(b)
        lst1[a].sort()

    s,g = map(int,input().split())

    result = 0

    def find_route(idx):
        global result
        if lst1[idx] == []:
            return
        if g in lst1[idx]:
            result = 1
            return
        for i in lst1[idx]:
            find_route(i)
    find_route(s)
    print(f"#{tc} {result}")