import sys
sys.stdin = open("input_color.txt","r")

T = int(input())
for t in range(T):
    n = int(input())
    arr= [list(map(int,input().split())) for _ in range(n)]

    result = {1:[], 2:[]}
    for i in range(n):
        for a in range(arr[i][0],arr[i][2]+1):
            for b in range(arr[i][1], arr[i][3]+1):
                result[arr[i][-1]].append((a,b))
    ans = len(set(result[1]) & set(result[2]))
    print(f"#{t+1} {ans}")
