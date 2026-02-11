n = int(input())
arr = [tuple(map(int,input().split())) for _ in range(n)]

# 위치[0] 기준으로 sort 가능
arr.sort()

lst = list(map(list,zip(*arr)))

# 최대 위치 값, 높이 찾기
max_idx = lst[1].index(max(lst[1]))
max_pnt = lst[0][max_idx]
max_height = lst[1][max_idx]

# print(max_idx, max_pnt, max_height)
# print(max_idx)
point, height = arr[0][0], arr[0][1]
check = arr[:max_idx+1]
area = max_height

for _ in range(2):
    now_p, now_h = check[0]
    for i,j in check :
        if j > now_h :
            area += now_h * abs(i - now_p)
            now_p, now_h = i,j
        else:continue

    check = arr[max_idx:][::-1]
print(area)
# for a,b in arr:

