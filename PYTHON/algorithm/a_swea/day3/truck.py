import sys
sys.stdin = open("input_truck.txt","r")


from collections import deque
def main(n,arr):
    rst = 0
    for i in range(n):
        check = [0] * 24
        q = deque()
        for d in range(arr[i][0],arr[i][1]):
            check[d] = 1
        q.append((i,1,check)) # 현재 idx, cnt
        while q:
            nidx, ncnt,ncheck = q.popleft()
            if ncnt > rst : rst = ncnt
            for j in range(i+1,n):
                if 1 in ncheck[arr[j][0] : arr[j][1]]:continue

                nxt = ncheck[:]
                for x in range(arr[j][0] ,arr[j][1]) :
                    nxt[x] = 1
                q.append((j,ncnt+1,nxt))

    return rst
T = int(input())
for tc in range(1,T+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    arr.sort()
    result = main(n,arr)
    print(f"#{tc} {result}")