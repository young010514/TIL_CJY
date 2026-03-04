import  sys
sys.stdin = open("input_cardgame.txt", "r")




from collections import deque
T  = int(input())
for tc in range(1,T+1):
    n = int(input())
    lst = list(map(int,input().split()))
    # data = []
    # for i in range(1,n+1):
    #     data.append((i,lst[i-1]))


    def fight(left, right):
        if (lst[left] - lst[right]) % 3 ==2 :
            return right
        else:return left

    def bfs(st, ed):
        if st == ed:
            return st
        left = bfs(st, (st + ed) // 2)
        right = bfs((st + ed) // 2 + 1, ed)
        return fight(left, right)

    winner = bfs(0,n-1) +1
    print(f"#{tc} {winner}")