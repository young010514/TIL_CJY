from collections import deque
n,m = map(int,input().split())
arr = [[] for _ in range(n+1)]
cnt = [0] * (n+1)
for _ in range(m):
    a,b = map(int,input().split())
    cnt[b] += 1
    arr[a].append(b)

used = [0] * (n+1)
def prt():
    for i in range(1,n+1):
        if cnt[i] == 0 and used[i]==0:
            used[i] = 1
            print(i,end=' ')
            for nxt in arr[i]:
                cnt[nxt] -=1
            return
for _ in range(n):
    prt()