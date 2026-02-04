T = int(input())
for t in range(T):
    n = int(input())
    arr =[list(map(int,input().split())) for _ in range(n)]
    # print(arr)
    # 최대 최소 초기값 설정
    max_data , min_data = -21e10, 21e10
    for i in range(n):
        for j in range(n):
            data = -arr[i][j]
            for k in range(n):
                data += (arr[i][k] + arr[k][j])
            max_data = data if data>max_data else max_data
            min_data = data if data <min_data else min_data
    print(f"#{t+1} {max_data - min_data}")