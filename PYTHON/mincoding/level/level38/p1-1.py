from collections import deque
st = int(input())
ed = int(input())
result = []
def remote(data, idx):
    if idx == 1:
        return data //2
    elif idx ==2:
        return data -1
    elif idx == 3:
        return data+1
    else:
        return data *2

q = deque()
q.append((st, 0))
while q:
    x ,cnt= q.popleft()
    if x == ed:
        print(cnt)
        q.clear()
        break
    gap = [abs(2*x-ed), abs(x+1-ed),abs(2//x-ed), abs(x-1-ed)]

