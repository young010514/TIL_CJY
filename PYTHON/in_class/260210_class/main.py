# 3묶음의 카드가 있을 때 한장씩 뽑았을때 나올 수 있는 모든 경우 다 출력

# card = "ABCD"
#
# def abc(level,path):
#     if level == 3:
#         print(*path)
#         return
#     for i in range(4):
#         path.append(card[i])
#         abc(level+1,path)
#         path.pop()
# abc(0,[])

# 순열 (한번뽑던 카드 또 안뽑기)
# path 배열 활용
# card = "ABCD"
#
# def abc(level,path):
#     if level == 3:
#         print(*path)
#         return
#     for i in range(4):
#         if card[i] not in path:
#             path.append(card[i])
#             abc(level+1,path)
#             path.pop()
# abc(0,[])

# visited 배열 활용

# card = "ABCD"
# path = [0] * 3
# visited = [0] * len(card)
#
# def abc(level):
#     if level == 3:
#         print(*path)
#         return
#     for i in range(4):
#         if visited[i] == 0:
#             # 함수 호출할때, path에 저장하고, visited  확인
#             path[level] = card[i]
#             visited[i] = 1
#
#             abc(level+1)
#             # 함수 리턴되었을 때 path 에서 빼고, visited 초기화
#             path[level] = 0
#             visited[i] = 0
# abc(0)

# 조합
# i + 1 부터 start 가 시작되면
# 예시
# A B C
# A B D
# A C D
# B C D
# card = "ABCD"
# path = [""] * 3

# def abc(level,start):
#     if level == 3:
#         print(*path)
#         return
#     for i in range(start,4):
#         path[level] = card[i]
#         abc(level+1, i+1)
#         path[level] =0
# abc(0,0)

# 중복조합
# i 부터 start 값이 시작되면
# A A A
# A A B
# A A C
# A A D
# A B B
# A B C
# A B D
# A C C
# A C D
# A D D
# B B B
# ...

card = "ABCD"
path = [""] * 3

def abc(level,start):
    if level == 3:
        print(*path)
        return
    for i in range(start,4):
        path[level] = card[i]
        abc(level+1, i)
        path[level] =0
abc(0,0)