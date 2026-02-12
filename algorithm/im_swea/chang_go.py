import sys
sys.stdin = open("input_changgo.txt" ,"r")

n = int(input())
arr = [tuple(map(int,input().split())) for _ in range(n)]

# 위치[0] 기준으로 sort 가능
arr.sort()

lst = list(map(list,zip(*arr)))
max_height= max(lst[1])

max_pnts=  []
for i in range(n):
    if lst[1][i] == max_height:
        max_pnts.append(i)

# left area 는  max_pnts[0] 보다 작은 구역
# right area 는  max_pnts[-1] 보다 큰 구역
left_arr = arr[:max_pnts[0]+1]
right_arr = arr[max_pnts[-1] :][::-1]
area = 0
lst1 = left_arr
for _ in range(2):
    prev_pnt = lst1[0][0]
    prev_height = lst1[0][1]
    for i in range(1,len(lst1)):
        now_pnt = lst1[i][0]
        now_height = lst1[i][1]
        if now_height > prev_height :
            area += prev_height * abs(prev_pnt - now_pnt)
            prev_height = now_height
            prev_pnt = now_pnt
    lst1 = right_arr
area += max_height * (arr[max_pnts[-1]][0] - arr[max_pnts[0]][0] +1)
print(area)