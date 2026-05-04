import sys
sys.stdin = open("input/in_1244.txt","r")

def dfs(depth):
    global Max

    if depth == b:
        Max = max(Max, int(''.join(map(str, a))))
        return

    key = (depth, tuple(a))
    if key in visited:
        return
    visited.add(key)

    for i in range(n-1):
        for j in range(i+1, n):
            a[i], a[j] = a[j], a[i]
            dfs(depth+1)
            a[i], a[j] = a[j], a[i]


T = int(input())
for tc in range(1, T+1):
    num, b = input().split()
    a = list(map(int, num))
    b = int(b)
    n = len(a)

    visited = set()
    Max = 0

    dfs(0)

    print(f'#{tc} {Max}')