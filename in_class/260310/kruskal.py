# Union find 자료 이용  크루스칼 알고리즘 구현

# 크루스칼 알고리즘 언제? 왜?

# 최소신장트리(Minimum spanning tree)
# == 무방향 그래프에 사이클 없이 연결된 구조
# prim, kruskal 알고리즘

# n,m = map(int,input().split())
# lines = []
# for _ in range(m):
#     a,b,c = input().split()
#     lines.append((a,b,int(c)))
#
# lines.sort(key=lambda x : x[2])

# print(arr)

n,m = map(int,input().split())

lines = [input().split() for _ in range(m)]
lines.sort(key=lambda x : int(x[2]))

arr = [0] * 200
rank = [0] * 200

result = 0
cnt = 0

def findboss(member):
    if arr[ord(member)] == 0: return member
    ret = findboss(arr[ord(member)])
    arr[ord(member)] = ret
    return ret

def Union(a,b,c):
    global result, cnt
    fa = findboss(a)
    fb = findboss(b)

    # 보스 같으면 연결 시 사이클 발생하므로 return 으로 꺼버리기
    if fa == fb : return

    # 연결 후 result 에 간선 가중치와 cnt 에 간선 개수 추가
    if rank[ord(fa)] > rank[ord(fb)] :
        arr[ord(fb)] = fa
    elif rank[ord(fa)] < rank[ord(fb)] :
        arr[ord(fa)] = fb
    else:
        rank[ord(fa)] += 1
        arr[ord(fb)] = fa
    result += c
    cnt += 1
    # 간선 개수가 노드-1개이면 함수 종료
    if cnt == n-1 : return

for i,j,d in lines:
    ret = Union(i,j,int(d))

print(result)
