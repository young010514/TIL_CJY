from collections import deque
n,m = map(int,input().split())
cnt = [0] * (n+1)
to =[[] for _ in range(n+1)]
used=[0] * (n+1)
for _ in range(m):
    a,b = map(int,input().split())
    cnt[b] += 1
    to[a].append(b)
q= deque()
for i in range(1,n+1):
    if cnt[i] ==0  :
        q.append(i)
        used[i] =1
while q:
    x = q.popleft()
    print(x,end=' ')
    if to[x]:
        for i in to[x]:
            if cnt[i] == 1 and used[i] == 0:
                used[i] =  1
                cnt[i] -= 1
                q.append(i)
                continue
            cnt[i] -= 1

