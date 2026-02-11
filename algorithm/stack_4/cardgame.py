import  sys
sys.stdin = open("input_cardgame.txt", "r")

T  = int(input())
for tc in range(1,T+1):
    n = int(input())
    lst = list(map(int,input().split()))
    user = [1]* n
    winner = -1

    print(f"\n#{tc} {winner+1}")
    def dfs(left,right):
        if right==left:
            print("bottom")
            return
        mid = (left+right) // 2
        dfs(left,mid)
        dfs(mid+1,right)
    dfs(0,n-1)


