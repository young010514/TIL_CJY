# n = int(input())
# time_wait = list(map(int,input().split()))
# time_wait.sort(reverse=True)
#
# answer = 0
# for i in range(1,n+1):
#     answer+= (i*time_wait[i-1])
# print(answer)
from collections import deque
n = int(input())
arr = [tuple(map(int,input().split())) for _ in range(n)]
arr.sort(key=lambda x: x[1])
# print(arr)
times = [0] * 25
cnt = 0
while  arr:
    st,ed = arr.pop()
    if times[ed] == 1: continue
    cnt +=1
    for i in range(st,ed):
        times[i] = 1
print(cnt)