import sys
sys.stdin = open('input_godae.txt', "r")

T= int(input())
for t in range(T):
    n,m = map(int,input().split())
    lst = [list(map(int,input().split())) for _ in range(n)]

    max_data = 0
    # for i in lst:
    #     print(*i)
    for i in range(n):
        for j in range(m):
            d, data = 0,0
            while i+d < n:
                if lst[i+d][j] == 1:
                    data += 1
                    if data > max_data:
                        max_data = data
                    d += 1
                else:
                    break

            d, data = 0, 0
            while j + d < m:
                if lst[i][j+d] == 1:
                    data += 1
                    if data > max_data:
                        max_data = data
                    d+=1
                else:
                    break
    print(f"#{t+1} {max_data}")