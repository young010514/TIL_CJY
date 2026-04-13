T = int(input())
for t in range(T):
    N,M=  map(int,input().split())
    arr = [list(input()) for _ in range(N)]
    result = ''
    for i in range(N):
        for j in range(N):
            xdata, ydata = True, True
            if i + M <= N :
                for d in range(M):
                    if arr[i + d][j] != arr[i + M - 1 - d][j]:
                            xdata = False
            else: xdata =False
            if j + M <= N:
                for d in range(M):
                    if arr[i][j+d] != arr[i][j + M - 1 - d]:
                        ydata = False
            else: ydata = False
            if xdata:
                result = ''.join([arr[i+d][j] for d in range(M)])
            if ydata:
                result = ''.join(arr[i][j:j+M])
    print(f"#{t+1} {result}")