# union find 자료구조
#  유사한 데이터들 끼리 묶어서 관리가 필요할 때 주로 사용

arr=[0]*200
rank=[0]*200



def findboss(member) :
    if arr[ord(member)] == 0:
        return member
    ret = findboss(arr[ord(member)])
    # 리턴될때 각 배열 값 갱신
    arr[ord(member)] = ret
    return ret

def Union(a, b):
    global arr
    aboss = findboss(a)
    bboss = findboss(b)
    if aboss == bboss:
        return

    # arr[ord(bboss)] = aboss

    # 보다 효율적으로 옮기기
    if rank[ord(aboss)] > rank[ord(bboss)] :
        arr[ord(bboss)] = aboss
    elif rank[ord(aboss)] > rank[ord(bboss)] :
        arr[ord(aboss)] = bboss
    else:
        arr[ord(aboss)] = bboss
        rank[ord(bboss)] += 1


Union('A','B')
Union('D','E')
Union('B','E')
Union('B','D')
Union('F','E')

y,x=input().split()
if findboss(y)==findboss(x):
    print("same")
else:
    print("different")




#
# def findboss(member):
#     if arr[member] == 0: return member
#     ret = findboss(arr[member])
#
#     arr[member] = ret
#     return ret
#
# def union(a,b):
#     fa = findboss(a)
#     fb = findboss(b)
#     if rank[fa] > rank[fb] :
#         arr[fb] = fa
#     elif rank[fa] < rank[fb] :
#         arr[fa] = fb
#     else:
#         arr[fa] = fb
#         rank[fb] += 1


# 사이클 여부 확인
n,m = map(int,input().split())
edge = []
for _ in range(m):  # 간선 정보 입력
    edge.append(input().split())

# 사이클 발생 여부를 확인할 수 있는 코드 완성해보기
arr = [0] * 200
result = 0
def findboss(member):
    if arr[ord(member)] == 0: return member
    ret = findboss(arr[ord(member)])
    arr[ord(member)] = ret
    return ret
def Union(a,b):
    global result
    ba = findboss(a)
    bb = findboss(b)
    # 사이클 발생
    if ba == bb :
        result = 1
        return
    arr[ord(bb)] = ba

for x,y in edge:
    Union(x,y)
    if result ==1 :
        print("cycle")
        break
if result == 0:print('no cycle')


# 싸이클 발생 여부를 확인할 수 있는 코드 완성해보기
# 5 5
# A B
# B C
# D E
# A D
# C D
#
# 입력시 "싸이클 발생" 출력


# 6 4
# A B
# B D
# F D
# A E
#
# 입력시 "싸이클 발생 안함" 출력











































