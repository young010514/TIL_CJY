# def abc(level):
#     if level == 2:
#         return
#     for i in range(2):
#         abc(level +1)
# abc(0)
arr  = ['a','b','c']
path = [''] * 2

# def abc(level):
#     if level == 2:
#         for i in range(2):
#             print(path[i], end=' ')
#         print()
#         return
#     for i in range(3):
#         path[level] += arr[i]
#         abc(level + 1)
#         # 앞에 들어왔던 코드를 지워주는 기능
#         path[level] = 0
# abc(0)


# arr  = ['a','b','c']
# path = [''] * 2
# def abc(level):
#     if level == 2:
#         print(*path)
#         return
#     for i in range(len(arr)):
#         path[level] = arr[i]
#         abc(level+1)
#
# abc(0)

N = int(input())
arr= [1,2,3,4,5,6]
path = [0] * N
cnt =0
def abc(level):
    global cnt
    if level == N:
        print(*path)
        cnt += 1
        return
    for i in range(len(arr)):
        path[level] = arr[i]
        abc(level+1)
        # path[i] = 0
abc(0)

print(cnt)

# 중복순열
