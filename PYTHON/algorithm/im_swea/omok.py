import sys
sys.stdin= open("input_omok.txt","r")

T = int(input())
for t in range(T):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    # default = 없음
    result = "NO"
    # 확인을 시작할 포인트 (i,j)
    for i in range(N):
        for j in range(N):
            data =["","","",""]
            for d in range(5):
                # 가로 확인
                if j + 4 <N:
                    data[0] += arr[i][j + d]

                # 세로 확인
                if i +4 < N:
                    data[1] += arr[i+d][j]

                # 대각선 확인
                if i+4 <N and j + 4 < N:
                    data[2] += arr[i+d][j+d]
                if i+4 < N and j-4 >= 0:
                    data[3] += arr[i+d][j-d]
            if "o"*5 in data:
                result = "YES"
                break


    print(f"#{t+1} {result}")