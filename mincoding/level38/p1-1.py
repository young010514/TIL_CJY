from collections import deque
st = int(input())
ed = int(input())
result = []
q = deque()
q.append((st, 0))
while q:
    x ,cnt= q.popleft()
    if x == ed:
        result.append(cnt)
        q.clear()
        break
    if x > 0 :q.append((x-1, cnt+1))
    if x <= 50000 : q.append((x*2,cnt+1))
    q.append((x+1,cnt+1))
    q.append((x//2, cnt +1))
print(min(result))