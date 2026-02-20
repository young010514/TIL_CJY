import  sys
sys.stdin = open("input_cardgame.txt", "r")

T  = int(input())
for tc in range(1,T+1):
    n = int(input())
    lst = list(map(int,input().split()))
    idx = list(range(n))

    n //=2
    while idx:

        result = []
        for i in range(n):
            left= idx[2*i]
            right= idx[2*i+1]
            if (lst[right]-lst[left]) % 3 == 1: result.append(right)
            else:result.append(left)

        result += idx[2*n:]

        if len(result) == 1:
            winner = result[0]+1
            break
        idx = result
        n = len(result) //2

    print(f"#{tc} {winner}")



