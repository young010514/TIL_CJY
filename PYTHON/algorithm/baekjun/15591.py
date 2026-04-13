from collections import deque
n,q = map(int,input().split())
arr = [[0] * (n+1) for _ in range(n+1)]
for _ in range(n-1):
    x,y,z = map(int,input().split())
    arr[x][y] = z
    arr[y][x] = z

def main(k,st):   # min value, start
    q = deque()
    q.append(st)  # 현재 노드
    used = [0] * (n+1)
    used[st] = 1
    cnt = 0
    while q :
        now = q.popleft()
        if now != st :
            cnt += 1
        for i in range(1,n+1):
            if arr[now][i] <k :continue
            if used[i] == 1: continue
            used[i]= 1
            q.append(i)

    return cnt



for _ in range(q):
    k,v = map(int,input().split())
    print(main(k,v))
