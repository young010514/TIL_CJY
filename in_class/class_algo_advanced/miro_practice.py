
# 0,0에서 4,4 까지의 최소 몇번이동해야 하는지 출력
# 보고지 않고, 참고하지 말고, 셤 본다 생각하고 해보시기를 바랍니다.
# 종이꺼내서 그림
# bfs 현재 위치에서 갈수 있는곳을 모두 QUEUE에 적는다.


# 미로찾기 문제
# DFS VS BFS
# 모든 경로를 탐색한다는 점에서 같다. (탐색 순서만 다르다)
# 하지만, DFS경우 탐색 후 RETURN(호출스택이 쌓임) 과정이 필요해서
# BFS 보다 수행시간이 더 많이 걸릴 수 있다. 그리고
# BFS 는 재귀의 구조가 아니라 QUEUE에 이동가능한 정보를 넣는 구조라서
# 원하는 정보가 QUEUE에 들어오면 바로 탐색을 중단하기 좋다 뿐만 아니라
# QUEUE에 먼저 들어오는 정보가 최소비용(값) 이 되기 때문에 비교적 효율적이라고 볼수 있다.
# 따라서 BFS가 DFS보다 나은 선택이다.

# BFS VS DIJKSTRA
# 정점간의 이동비용이 1이 아니라면 (2, 6 등..) DIJKSTRA 알고리즘이 효율적일 수 있으나
# 정점간의 이동비용이 1이라면 BFS가 시간복잡도상 더 나은 선택이 될수 있다.
# BFS는 시간복잡도가 O(정점의개수+간선의개수) 라면
# DIJKSTRA는 시간복잡도가 O(NlogN(, N=정점*간선)) 이라서 따지자면, BFS가 더 빠르다.

# 결론: 미로찾기 문제 + 가중치가 1 이라면 BFS
#       미로찾기 문제 + 가중치가 1 이상이라면 DIJKSTRA

# BFS
from collections import deque
arr = [
    [0,0,1,0,0],
    [0,0,1,0,0],
    [0,1,1,1,0],
    [0,0,1,0,1],
    [0,0,0,0,0]
]
dts = [(0,1),(0,-1),(1,0),(-1,0)]
q = deque()
q.append((0,0,0))  # x,y, cnt
while q:
    nx,ny,cnt = q.popleft()
    if nx==4 and ny == 4 :
        result = cnt
        break
    for i,j in dts:
        dx = nx +i
        dy = ny +j
        if dx <0 or dx >4 or dy<0 or dy>4 : continue
        if arr[dx][dy] ==1 : continue
        arr[dx][dy] = 1
        q.append((dx,dy,cnt+1))
print(result)

# Dijkstra
