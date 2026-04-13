from collections import deque
t = int(input())
for tc in range(1,t+1):
    n = int(input())
    arr = [tuple(map(int,input().split())) for _ in range(n+2)]
    def main(arr):
        q = deque()
        st = arr[0]
        q.append(st)
        ed = arr[-1]
        stores = arr[1:n+1]   # 편의점들
        used = [0] * n
        result = "sad"
        while q :
            nx,ny = q.popleft()
            if abs(ed[0] - nx ) + abs(ed[1] - ny) <= 1000:
                result = "happy"
                break
            for i in range(n):
                if used[i] == 1 : continue
                if abs(stores[i][0]-nx) + abs(stores[i][1]-ny) > 1000 : continue
                used[i] = 1
                q.append(stores[i])

        return result
    print(main(arr))
