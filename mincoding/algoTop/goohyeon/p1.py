n = int(input())
arr = [int(input()) for _ in range(n)]
lst = [0] * n
for i in range(1,n):
    if arr[i] - arr[i-1] > 0:
        lst[i] = arr[i] - arr[i-1]
if sum(lst) ==0 :print(0)
else:
    idx = lst.index(max(lst))
    print(idx, idx +1)