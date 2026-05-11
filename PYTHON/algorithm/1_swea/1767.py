import sys
sys.stdin =open("input/in_1767.txt","r")

def dfs(level,now,n):
    if level == n:
        return


def main(n,arr):
    cores = []
    for i in range(1,n-1):
        for j in range(1,n-1):
            if arr[i][j] == 1: cores.append((i,j))
    dfs(0,cores[0],len(cores))






T = int(input())
for tc in range(1,T+1):
    n =int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    main(n,arr)