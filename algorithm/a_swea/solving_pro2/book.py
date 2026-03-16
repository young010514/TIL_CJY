import sys
sys.stdin = open("input_book.txt","r")


T = int(input())
for tc in range(1,T+1):
    n,b=map(int,input().split())
    arr =list(map(int,input().split()))
    arr.sort(reverse=True)
    result = 21e8
    def dfs(now, hsum):
        global  result
        if hsum >= b :
            if result > hsum-b:
                result= hsum-b
            return
        for i in range(now+1,n):
            dfs(i,hsum + arr[i])

    dfs(-1,0)
    print(f"#{tc} {result}")