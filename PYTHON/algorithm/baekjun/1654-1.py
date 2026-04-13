import math
k,n = map(int,input().split())
arr = [int(input()) for _ in range(k)]
def check(data):
    cnt = 0
    for a in arr:
        cnt += a // data
    return cnt >= n

def main():
    left = 1
    right = max(arr)
    while left <= right:
        mid = (left+right) // 2
        if check(mid):
            result = mid
            left = mid + 1
        else:
            right = mid -1
    return result
result = main()
print(result)