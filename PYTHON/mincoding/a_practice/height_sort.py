import sys
sys.stdin = open("input/input_height.txt","r")

from collections import deque
def main(node):
    used = [0] * (n+1)
    ret = 0
    arr = high
    for _ in range(2):
        q = deque([node])
        while q:
            now = q.popleft()
            for i in arr[now]:
                if used[i] == 1 : continue
                used[i] =1
                ret += 1
                q.append(i)
        used = [0] * (n+1)
        arr=low
    return ret


T = int(input())
for tc in range(1,T+1):
    n = int(input())
    m = int(input())
    high = [[] for _ in range(n+1)]
    low = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b = map(int,input().split())
        high[a].append(b)
        low[b].append(a)
    ans =0
    for i in range(1,n+1):
        if main(i) == n-1 : ans += 1



    print(f"#{tc} {ans}")