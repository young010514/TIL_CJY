import math
k,n = map(int,input().split())
arr = [int(input()) for _ in range(k)]
Min = min(arr) // (math.ceil(n/k))
Max = sum(arr) // n
def check(data):
    cnt = 0
    for a in arr:
        cnt += a // data
    if cnt >= n : return 1
    else : return 0

def dfs(left,right):
    global result
    mid = (left + right) // 2
    if right - left <= 1:
        if check(right) == 1: result = right
        else : result= left
        return

    x = check(mid)
    if x ==1: dfs(mid,right)
    elif x == 0: dfs(left,mid)

dfs(Min,Max)
print(result)