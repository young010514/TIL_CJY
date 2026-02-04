# 버블 정렬

# n = int(input())
# lst = list(map(int,input().split()))
# sorted = False
# while sorted ==False:
#     sorted = True
#     for i in range(len(lst)-1):
#         if lst[i] > lst[i+1]:
#             lst[i], lst[i+1] = lst[i+1], lst[i]
#             sorted = False
# print(*lst)

# A = "TEMSIYTNHASDOF"
# A = input()
# B = input()
# C = list(A[:])
# ans = -1
#
# for i in list(B):
#     if i in C :
#         idx = C.index(i)+1
#         ans += idx
#         C = C[idx:]
#     else:
#         ans = -1
#         break
#
# print(ans)


# 좌표 입력 받고 위아래 좌우의 합을 출력
# dirs=[
#     (-1,0),
#     (1, 0),
#     (0, -1),
#     (0, 1),
# ]
#
# arr =[
#     [3,5,4],
#     [1,1,2],
#     [1,3,9],
# ]
# x,y = map(int,input().split())
# sum = 0
# for i,j in dirs:
#     if 0 <= x + i  <3 and 0<= y+j < 3:
#         sum += arr[x+i][y+j]
# print(sum)



# 입력받은 좌표값의 대각선에 있는 값들의 곱 구하기

# arr = [ [3, 5, 4, 5, 6],
#         [1, 1, 2, 7, 8],
#         [1, 2, 9, 1, 2],
#         [3, 5, 4, 5, 6],
#         [1, 1, 2, 7, 8]]
#
# x,y=map(int,input().split())
#
# dir = [
#     (1,1),
#     (1,-1),
#     (-1,-1),
#     (-1,1),
# ]
# result = 1
# for i,j in dir:
#     if 0 <= x+i < len(arr) and 0 <= y+j < len(arr[0]):
#         result *= arr[x+i][y+j]
# print(result)

# 크레이지아케이드

# arr = [ [3, 5, 4, 5, 6],
#         [1, 1, 2, 7, 8],
#         [1, 2, 9, 1, 2],
#         [3, 5, 4, 5, 6],
#         [1, 1, 2, 7, 8]]
#
# dirs = list(range(-3,4))
# x,y = map(int,input().split())
# result = -2*arr[x][y]
#
# for d in range(-3,4):
#     if 0 <= x + d < len(arr):
#         result += arr[x+d][y]
#     if 0 <= y + d < len(arr[0]):
#         result += arr[x][y+d]
#
# print(result)
#



# 위아래좌우 좌표들의 합이 가장 큰 곳의 합과. 좌표값 출력하기

# arr=[[1,2,3,4],
#     [1,2,9,4],
#     [1,9,3,9],
#     [1,2,9,4]]

directions = [
    (-1,0),
    (1,0),
    (0,1),
    (0,-1),
]
arr= [list(map(int,input().split())) for _ in range(4)]
max_data = -21e10
idx = 0,0
for i in range(len(arr)):
    for j in range(len(arr[0])):
        result = 0
        for x,y in directions :
            if 0 <= x + i <len(arr) and 0 <= y+j <len(arr[0]):
                result += arr[x+i][y+j]
        if result > max_data:
            max_data = result
            idx = i,j

print(max_data)
print(idx)


# 1 2 3 4
# 1 2 9 4
# 1 9 3 9
# 1 2 9 4