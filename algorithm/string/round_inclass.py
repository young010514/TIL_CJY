import sys
sys.stdin = open("input_round.txt","r")

T = int(input())
for t in range(T):
    result = ""
    n,m=  map(int,input().split())
    arr = [list(input()) for _ in range(n)]

    # zip 함수를 활용해서
    for _ in range(2):
        # 가로 먼저 확인
        for i in range(n):
            for j in range(n-m+1):
                st = arr[i][j:j+m]
                if st == st[::-1] :
                    result = ''.join(st)
        arr = list(map(list,zip(*arr)))
    print(f"#{t+1} {result}")