from collections import deque
n,m = map(int,input().split())
arr = [0] * 101
used = [0] * 101
for _ in range(n+m):
    x,y = map(int,input().split())
    arr[x] = y


q = deque()
q.append((1,0))   # now, cnt
result = 0
while q :
    now, cnt = q.popleft()
    if now == 100 :
        result = cnt
        break
    for i in range(6,0,-1):
        if now + i > 100 : continue
        if used[now+i] == 1 : continue
        if arr[now+i] !=0 and used[arr[now+i]] ==1 : continue
        if arr[now+i]== 0:
            used[now+i] =1
            q.append((now+i, cnt+1))
        else:
            used[arr[now + i]] = 1
            q.append((arr[now+i], cnt+1))
print(result)

