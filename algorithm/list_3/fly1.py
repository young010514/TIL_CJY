import sys
sys.stdin = open("input_fly1.txt", "r")

T = int(input())
for t in range(T):
    n,m = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    max_data = -21e10

    directions = []
    for x in range(m):
        for y in range(m):
            directions.append((x,y))

    for i in range(n-m+1):
        for j in range(n-m+1):
            data = 0
            for x,y in directions :
                data += arr[i+x][j+y]
            if data > max_data : max_data = data
    print(f"#{t+1} {max_data}")

