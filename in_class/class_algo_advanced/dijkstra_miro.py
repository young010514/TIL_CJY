import heapq
st = (0,0)
ed = (3,2)
arr = [
    [0,4,8,29,99],
    [6,-1,4,-1,7],
    [42,-1,2,-1,4],
    [2,3,2,8,5],
]
dirts =[(0,1),(0,-1),(1,0),(-1,0)]
inf = 21e8


result = [[inf]*5 for _ in range(4)]
result[0][0] = 0
heap = [(0,0,0)]
ans = inf
while heap :
    price ,x,y = heapq.heappop(heap)

    if x == 3 and y == 2:
        ans = price
        break

    for i,j in dirts:
        dx = x + i
        dy = y + j
        if dx < 0 or dy <0 or dx > 3 or dy > 4:continue
        if arr[dx][dy] ==-1:continue

        cost = price + arr[dx][dy]
        if cost < result[dx][dy] :
            result[dx][dy] = cost
            heapq.heappush(heap,(cost,dx,dy))
print(ans)









