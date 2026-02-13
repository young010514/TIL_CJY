import sys
sys.stdin =open("input_charbomba.txt" ,"r")

T = int(input())
for tc in range(1,T+1):
    n,p = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    max_data = 0
    for i in range(n):
        for j in range(n):
            data = -arr[i][j]
            for d in range(-p, p +1):
                if 0<= i + d  < n : data += arr[i+d][j]
                if 0<= j + d  < n : data += arr[i][j+d]
            if max_data < data : max_data =data
    print(f"#{tc} {max_data}")