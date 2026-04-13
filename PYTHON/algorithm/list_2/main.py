# lst=[4,3,5,1,7,5,6,8,1,6,9,5]
# # target 이라는 리스트에 0~7 사이의 정수 3개 입력받기
# # n 이라는 변수에 1~5 사이의 정수를 입력받기
# target = list(map(int,input().split()))
# n = int(input())
# 입력받은 정수로 부터 연속된 n개의 정수의 합이
# 맥스일때의 정수값과 max값을 출력하시오

# max_data=target[0]
#
# for tar in target:
#     sum_data =0
#     for j in range(n):
#         sum_data += lst[tar+j]
#     if max_data < sum_data:
#         idx = tar
#         max_data = sum_data
# print(f'{idx} {max_data}')
#
# Max = -21e8
# M_target = 0
# def getSum(start):
#     Sum = 0
#     for i in range(start , start+n):
#         Sum += lst[i]
#     return Sum
#
# for i in range(len(target)):
#     ret = getSum(target[i])
#     if Max < ret :
#         Max = ret
#         M_target = target[i]
# print(M_target, Max)
# 예를들어 target 리스트에 정수 1 5 3 을 입력받은 후
# n값으로 4를 입력을 받았을 경우


# 1번 인덱스로 부터 연속된 4개(n개)의 합은 16 이고
# 5번 인덱스로 부터 연속된 4개(n개)의 합은 20 이며
# 3번 인덱스로 부터 연속된 4개(n개)의 합은 19 입니다.


# 따라서 합이 맥스 일때의 정수값은 두번째로 입력받은 5 이며
# max값은 20 입니다.


# 입력예제
# 1 5 3
# 4
#
# 출력예제
# 5 20


# ================================================


# 연속되는 숫자 3개의 합이 가장 클 때 의 값을 출력해 주세요
lst= [[4, 5, 2, 6, 7, 3, 1],
      [2, 9, 9, 6, 1, 6, 7]]

# def getSum(arr):
#     Max_sum = -21e9
#     for i in range(len(arr)-2):
#         Sum = 0
#         for j in range(3):
#             Sum += arr[i+j]
#         if Sum > Max_sum:
#             Max_sum = Sum
#
#     return Max_sum
#
# result = -11e11
# for i in lst:
#     if result < getSum(i):
#         result = getSum(i)
# print(result)

# 강사님 풀이

# Max = -22e25
# def getSum(x,y):
#     Sum = 0
#     for i in range(3):
#         Sum += lst[x][y+i]
#     return Sum
# for i in range(2):
#     for j in range(5):
#         Sum = getSum(i,j)
#         if Max < Sum:
#             Max = Sum
# print(Max)


# ================================================================

# 1 2 3 4 5
# 2 4 2 1 3
# 3 4 5 2 5
#
# 3 4 5 라는 패턴이 어느 좌표에 있는지 찾기!!
#
# 정답은:
# 0,2
# 2,0

# lst=[[1 ,2 ,3 ,4 ,5],
#      [2 ,4 ,2 ,1 ,3],
#      [3 ,4 ,5 ,2 ,5]]
#
# target=[3, 4, 5]
#
# def find(lst, target):
#     result =[]
#     for i, inner in enumerate(lst):
#         for j in range(len(inner) - len(target) + 1):
#             if lst[i][j] == target[0]:
#                 bool_data = True
#                 for d in range(1,len(target)):
#                     if lst[i][j+d] != target[d]:
#                         bool_data = False
#                 if bool_data: result.append((i,j))
#     return result
# result = find(lst, target)
# for x,y in result:
#     print(x,y)



board = [
    ["A", "B", "G", "K"],
    ["T", "T", "A", "B"],
    ["A", "C", "T", "T"]
]
# ptn = [list(input().split()) for _ in range(2)]

# A B
# T T
# 발견2개
#
# G K
# A B
# 발견1개
#
# A B
# C D
# 미발견


# cnt =0
# def findStr(x,y):
#     for i in range(2):
#         for j in range(2):
#             if board[x+i][y+j] != ptn[i][j]:
#                 return 0
#     return 1
#
# for x in range(2):
#     for y in range(3):
#         if findStr(x,y):
#             cnt += 1
#
# print(cnt)



# =============================
a = [3,8,5,2,5,7,2,4]
bucket = [0]*10
n = int(input())
b= list(map(int,input().split()))

for i in range(len(a)):
    bucket[a[i]] +=1

for i in range(n):
    print(f"{b[i]}가 {bucket[b[i]]}개 있음")