import sys
sys.stdin= open("input/in_2115.txt","r")

def main(lst, m,c):
    max_p=0

    def dfs(idx, current_sum, current_profit):
        nonlocal max_p
        if current_sum > c:
            return
        max_p = max(max_p, current_profit)
        if idx == m:
            return

        # 현재 벌통을 선택하는 경우
        dfs(idx + 1, current_sum + lst[idx], current_profit + lst[idx] ** 2)
        # 선택하지 않는 경우
        dfs(idx + 1, current_sum, current_profit)

    dfs(0, 0, 0)
    return max_p


T= int(input())
for tc in range(1,T+1):
    n,m,c = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    result = [[0] * n  for _ in range(n)]
    for i in range(n):
        for j in range(n-m+1):
            result[i][j] = main(arr[i][j:j+m], m,c)
    ans = 0
    for r1 in range(n):
        for c1 in range(n-m+ 1):
            # 두 번째 일꾼 탐색
            for r2 in range(r1, n):
                # 첫 번째 일꾼과 같은 행인 경우, 겹치지 않도록 c2 시작점 조절
                start_c2 = c1 + m if r1 == r2 else 0
                for c2 in range(start_c2, n-m + 1):
                    ans = max(ans, result[r1][c1] + result[r2][c2])
    print(f'#{tc} {ans}')

