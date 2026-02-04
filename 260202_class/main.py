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

arr = [ [3, 5, 4, 5, 6],
        [1, 1, 2, 7, 8],
        [1, 2, 9, 1, 2],
        [3, 5, 4, 5, 6],
        [1, 1, 2, 7, 8]]

x,y=map(int,input().split())

dir = [
    (1,1),
    (1,-1),
    (-1,-1),
    (-1,1),
]
result = 1
for i,j in dir:
    if 0 <= x+i < len(arr) and 0 <= y+j < len(arr[0]):
        result *= arr[x+i][y+j]
print(result)