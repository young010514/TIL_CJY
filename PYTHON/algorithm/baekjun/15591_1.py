from collections import deque
n,q = map(int,input().split())
arr = [[] for _ in range(n+1)]
for _ in range(n-1):
    x,y,z = map(int,input().split())
    arr[x].append((y,z))
    arr[y].append((x,z))


def main(k,st):   # min value, start
    q = deque()
    q.append(st)  # 현재 노드
    used = [0] * (n+1)
    used[st] = 1
    cnt = -1
    while q :
        now = q.popleft()
        cnt += 1
        for i in arr[now]:
            nxt = i[0]
            if used[nxt] ==1 :continue
            if i[1] < k :continue
            used[nxt] = 1
            q.append(nxt)


    return cnt



for _ in range(q):
    k,v = map(int,input().split())
    print(main(k,v))
