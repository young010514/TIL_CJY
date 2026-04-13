# arr = [
#     [0,1,1,0,0],
#     [0,0,0,0,0],
#     [1,0,0,0,1],
#     [1,0,0,0,1],
#     [1,0,0,0,0]
# ]
# # 누가 가장 인기가 많은가?
# result = -190
# idx = -10
# for j in range(5):
#     data = 0
#     for i in range(5):
#         data += arr[i][j]
#     if data > result:
#         result = data
#         idx = j
# print(idx)
#
#
# name = ['A','B','E','C','D','F']


# name=['A','B','E','C','D','F']
# n,m=map(int,input().split())
# arr=[[] for _ in range(n)]
# for i in range(m):
#     a,b=map(int,input().split())
#     arr[a].append(b)
#
# test=1

# 6 5
# 0 1
# 0 2
# 1 3
# 1 4
# 2 5
# name=['A','B','E','C','D','F']
# n,m=map(int,input().split())
# arr=[[] for _ in range(n)]
# for i in range(m):
#     a,b=map(int,input().split())
#     arr[a].append(b)
#
# def dfs(now):
#
#     print(name[now],end=' ')
#
#     for i in arr[now]:
#         dfs(i)
#
#
# dfs(0) # 0번 인덱스 부터 dfs 시작



# name =list("BACD")
# arr = [
#     [0,1,1,0,],
#     [1,0,1,1],
#     [0,1,0,1],
#     [0,0,0,0]
# ]
# visited = [0]*4
# def dfs(now):
#     print(name[now],end=' ')
#     for i in range(4):
#         if arr[now][i] == 1 and visited[i] == 0:
#                 visited[i] = 1
#                 dfs(i)
# visited[0] =1
# dfs(0)

# 경로 찾기
#
# name = list('BACD')
# arr = [
#     [0,1,1,0],
#     [0,0,1,1],
#     [0,1,0,1],
#     [0,0,0,0]
# ]
# visited = [0]*4
# cnt =0
# def dfs(now):
#     global cnt
#     if name[now] == "D":
#         cnt +=1
#         # return
#     for i in range(4):
#         if arr[now][i] == 1 and visited[i] == 0:
#             visited[i] = 1
#             dfs(i)
#             visited[i] = 0
# visited[0] = 1
# dfs(0)
# print(cnt)

# 가중치가 있는 경우
# 한 정점에서 다른 정점까지의 최소 비용을 dfs 로 구해보기
name = list('BACD')
# arr = [
#     [0,3,7,0],
#     [0,0,1,9],
#     [0,1,0,2],
#     [0,0,0,0]
# ]
# used = [0]*4
# Min = 21e10

# def dfs(now,Sum):
#     global Min
#     if now == 3:
#         if Sum < Min :
#             Min = Sum
#
#     for i in range(4):
#         if arr[now][i] > 0 and used[i] == 0:
#             used[i] = 1
#             dfs(i,Sum + arr[now][i])
#             used[i] = 0
# used[0] =1
# dfs(0,0)
# print(Min)


# 인접 리스트를 통해 가중치가 있는 무방향 그래프
# name = list('BACD')
# arr = [
#     [(1,3), (2,8)],
#     [(0,3),(2,1),(3,8)],
#     [(0,8),(1,1),(3,1)],
#     [(1,8),(2,1)],
# ]
# visited = [0]* 4
# Min = 21e10
# def dfs(now,Sum):
#     global Min
#     if now == 3 and Sum < Min:
#         Min = Sum
#
#     for i,j in arr[now]:
#         if visited[i] == 0:
#             visited[i] = 1
#             dfs(i, Sum + j)
#             visited[i]=0
# dfs(0,0)
# print(Min)



# 위에서 부터 한칸 씩 내려오면서
# 숫자 한개씩을 선택합니다,
# 선택한 숫자들을 모두 더했을 때
# 합이 20 이상인 경우가 몇가지 인지 출력해 주세요

# arr=[[4,5,2],
#      [-2,1,6],
#      [3,9,-4],
#      [3,5,2]]
# cnt = 0
# def dfs(level, Sum):
#     global cnt
#     if level == 4:
#         if Sum >= 20 : cnt += 1
#         return
#     for i in range(3):
#         dfs(level +1, Sum + arr[level][i])
# dfs(0,0)
# print(cnt)

# 위에서 부터 한칸 씩 내려오면서
# 숫자 한개씩을 선택합니다.
# 계단을 밑으로 내려오면서 이동할 수 있는 범위는
# 7시방향 6시방향 5시방향 입니다.
# 선택한 숫자들을 모두 더했을 때
# 합이 30 이상인 경우가 몇가지 인지 출력해 주세요

arr=[[3,5,9,6],
     [7,-8,1,6],
     [-10,2,3,9],
     [5,1,2,8],
     [4,7,1,8]]
cnt = 0
def dfs(x,y, Sum):
    Sum += arr[x][y]
    global cnt
    if x == 4:
        if Sum >= 30 :
            cnt += 1
        return
    for i in range(-1,2):
        if 0 <= y + i  < 4:
            dfs(x+1, y+i, Sum)
for j in range(4):
    dfs(0,j,0)
print("cnt",cnt)




# 위에서 부터 한칸 씩 내려오면서
# 숫자 한개씩을 선택합니다.
# 계단을 밑으로 내려오면서 이동할 수 있는 범위는
# 7시방향 6시방향 5시방향 입니다.
# 선택한 숫자들을 모두 더했을 때
# 합이 30 이상인 경우가 몇가지 인지 출력해 주세요

arr=[[3,5,9,6],
     [7,-8,1,6],
     [-10,2,3,9],
     [5,1,2,8],
     [4,7,1,8]]
cnt = 0
def dfs(x,y, Sum):
    global cnt
    if x == 4:
        if Sum >= 30 :
            cnt += 1
        return
    for i in range(-1,2):
        if 0 <= y + i  < 4:
            dfs(x+1, y+i, Sum + arr[x+1][y+i])
for j in range(4):
    dfs(0,j,arr[0][j])
print("cnt",cnt)
