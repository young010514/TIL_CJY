# 개발을 착수한 곳의 위 아래 좌 우 그리고 자기자신의 좌표의 값이
# *7 한 후 %10 한 값으로 바뀐다고 합니다.
# 총 3번의 개발 후 3*3 사이즈의 땅의가치를 모두 더했을떄
# 최대 이익은 몇일까요? (중복가능)
# arr = [list(map(int,input().split())) for _ in range(3)]
arr=[[4,7,2],[5,3,9],[6,1,8]]
directions = [(0,0),(0,1),(0,-1),(1,0),(-1,0)]
Max = -2e5
# def dfs(level,path):
#     if level == 3:
#         global Max
#         Sum = 0
#         for inner in arr:
#             Sum += sum(inner)
#         if Sum > Max :
#             print(path)
#             Max = Sum
#         return
#     for i in range(9):
#         x,y  = i //3 , i % 3
#         for i,j in directions:
#             if 0<=x+i<3 and 0<= y+j <3:
#                 raw = arr[x+i][y+j]
#                 path.append((x+i,y+j))
#                 arr[x+i][y+j] = (raw * 7) % 10
#                 dfs(level + 1,path)
#                 path.pop()
#                 arr[x + i][y + j] = raw
# dfs(0,[])
# print(Max)


from copy import deepcopy
arr=[[4,7,2],[9,6,3],[6,1,5]]
Max = -2e5

def digging(x,y):
    directx = [0,0,-1,1,0]
    directy = [ -1, 1, 0,0,0]
    for i in range(5):
        dx = x + directx[i]
        dy = y + directy[i]
        if 0 <= dx < 3 and 0 <= dy < 3:
            arr[dx][dy] = (arr[dx][dy] * 7) % 10

def dfs(level):
    global  arr, Max

    # 2차원 배열이니까 deepcopy 활용 /이때 digging 하기 전에 원본 복사해둘것!
    raw = deepcopy(arr)
    if level == 3:
        data =0
        for i in arr:
            data += sum(i)
        if data > Max: Max = data
        return
    for i in range(3):
        for j in range(3):
            digging(i,j)
            dfs(level + 1)
            # 원상복구
            arr = deepcopy(raw)

dfs(0)
print(Max)