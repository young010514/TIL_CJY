import sys
sys.stdin = open("input_changgo.txt","r")

# 강사님 풀이

n = int(input())
arr = [0] * 1001
for i in range(n):
    l,h = map(int,input().split())
    arr[l] = h
# 가장 높은 곳 idx 찾기
best_idx = 0
Max = 0
for i in range(1001):
    if arr[i] > Max :
        Max = arr[i]
        best_idx = i

# brick이 시작되는 인덱스 찾기
st_idx = 0
for i in range(1001):
    if arr[i] != 0 :
        st_idx = i
        break

# 마지막 brick의 인덱스 찾기
ed_idx = 0
for i in range(1000,-1,-1):
    if arr[i] != 0 :
        ed_idx = i
        break

# 면적 더하기
area = 0
# 왼쪽에서 start
nowh = arr[st_idx]
for i in range(st_idx, best_idx+1) :
    if nowh < arr[i] :
        nowh = arr[i]
    area += nowh


# 오른쪽에서 start
nowh = arr[ed_idx]
for i in range(ed_idx, best_idx,-1) :
    if nowh < arr[i] :
        nowh = arr[i]
    area += nowh
print(area)