# 순열

arr = ['A', 'B', 'C', 'D']
path = [''] * 3
used = [0] * 4


# def abc(level):
#     # global used,path      # 안써도 되는 이유?
#           #
#
#     if level == 3:
#         print(*path)
#         return
#     for i in range(4):
#         if used[i] == 1: continue
#         used[i] = 1  # 방문 체크
#         path[level] = arr[i]  # 경로 기록
#         abc(level + 1)
#         path[level] = ''  # 방문 삭제
#         used[i] = 0  # 경로 삭제
#
# abc(0)


# A,B,C,D 가 적힌 카드 묶음이 3개 있을 때
# 각각의 묶음에서 카드를 뽑았을때 나올 수 있는 모든 경우 출력 (중복순열)

# 조건 : 첫번째 카드에서 "B"가 나오지 않는 경우를 다 출력하기

# arr = ['A', 'B', 'C', 'D']
# path = [''] * 4
# cnt =0
# def abc(level):
#
#     # 진입 후 리턴되는 버젼
#     if path[0] == "B" : return
#     global  cnt
#     if level == 4:
#         cnt +=1
#         return
#     for i in range(4):
#         path[level] = arr[i]
#         abc(level+1)
#         path[level] =''
# abc(0)
# print(cnt)
#
#
# # 조건 : 첫번째 카드에서 "B"가 나오지 않는 경우를 다 출력하기
# # 진입 자체를 막는 버젼 , if level == 0 and i == 1 : continue
#
# arr = ['A', 'B', 'C', 'D']
# path = [''] * 4
# cnt =0
# def abc(level):
#     global  cnt
#     if level == 4:
#         cnt +=1
#         print(*path)
#         return
#     for i in range(4):
#         if level == 0 and i == 1: continue
#         path[level] = arr[i]
#         abc(level+1)
#         path[level] =''
# abc(0)
# print(cnt)


# 어떠한 경우라도 "C"가 나오면 안됨
# 진입이 안되는 경우
# arr = ['A', 'B', 'C', 'D']
# path = [''] * 3
# def abc(level):
#     if level == 3:
#         print(*path)
#         return
#     for i in range(4):
#         if i == 2: continue
#         path[level] = arr[i]
#         abc(level+1)
#         path[level] = ''
# abc(0)
# print("*****************************")
# # 어떠한 경우라도 "C"가 나오면 안됨
# # 진입 후 리턴
#
# arr = ['A', 'B', 'C', 'D']
# path = [''] * 3
# def abc(level):
#     # if "C" in path : return
#     if level > 0 and path[level-1] == "C" : return
#     if level == 3:
#         print(*path)
#         return
#     for i in range(4):
#         path[level] = arr[i]
#         abc(level+1)
#         path[level] = ''
#
# abc(0)


# 연속해서 같은 카드가 2장 나오면 안됨
# 진입 막기

arr = ['A', 'B', 'C', 'D']
path = [''] * 3
def abc(level):
    if level == 3:
        print(*path)
        return
    for i in range(4):
        path[level] = arr[i]
        if level > 0 and path[level -1] == arr[i] : continue
        abc(level+1)
        path[level]= ''
# abc(0)


arr = ['A', 'B', 'C', 'D']
path = [''] * 3
def abc(level):
    if level > 1 and path[level-1] == path[level-2] : return
    if level == 3:
        print(*path)
        return
    for i in range(4):
        path[level] = arr[i]
        abc(level+1)
        path[level]= ''

abc(0)