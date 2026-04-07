n,k = map(int,input().split())
arr = [int(input()) for _ in range(n)]
# arr.sort()
result = [10009] * (k+1)
result[0] = 0
def dp():
    global result
    for d in arr:
        for i in range(d,k+1):
            if result[i] == -1 or result[i] > result[i-d] + 1:
                result[i] = result[i-d] + 1
dp()
if result[k] >= 10009 : result[k] = -1
print(result[-1])