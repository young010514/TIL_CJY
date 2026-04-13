# dfs (이진트리 dfs 탐색)
arr = " ABCDE F"
def dfs(now):
    # 배열 범위 넘어가거나 공백인 경우
    if now >= len(arr) or arr[now] == " " : return
    print(arr[now], end=' ')
    dfs(now*2)      # 왼쪽 자식
    dfs(now*2 + 1)  # 오른쪽 자식
dfs(1)  # A B D E C F

print("\nBFS")
# bfs
arr = " ABCDE F"
from collections import deque
def bfs(now):
    q= deque()
    q.append(now)
    while q:
        x = q.popleft()
        print(arr[x],end=' ')
        if x * 2 < len(arr) and arr[x*2] != " ":
            q.append(x*2)
        if x*2 +1 < len(arr) and arr[x*2 +1] !=" ":
            q.append(x*2+1)
bfs(1)

print('\npre order')
# pre order
arr = " ABCDE F"
def pre_order(now):
    if now >= len(arr) or arr[now] == " " : return
    print(arr[now],end=' ')
    pre_order(2*now)
    pre_order(2*now+1)
pre_order(1)



print('\npost order')
# post order
arr = " ABCDE F"
def post_order(now):
    if now >= len(arr) or arr[now] == " " : return
    post_order(2*now)
    post_order(2*now+1)
    print(arr[now],end=' ')
post_order(1)

print('\nin order')
# in order
arr = " ABCDE F"
def in_order(now):
    if now >= len(arr) or arr[now] == " " : return
    in_order(2*now)
    print(arr[now],end=' ')
    in_order(2*now+1)
in_order(1)

print("\n\nInsert")
arr = [0] * 20  # 넉넉하게 20칸짜리
lst=[4,2,9,7,15,1,3]    # 저장할 데이터
# 함수 2개 만들것
# insert 함수 - tree 모양으로 데이터 저장
# search 함수 - tree 를 탐색하는 함수

arr=[0]*20 # 넉넉하게 20칸 짜리 만듬
lst=[4,2,9,7,15,1,3] # 저장할 데이터

def Insert(target): # 트리 모양으로 데이터 저장
    now=1 # 루트노드 1번 인덱스에 저장
    while 1:
        if arr[now]==0:
            arr[now]=target
            return
        if arr[now] < target:
            now=now*2+1
        else:
            now=now*2



def Search(target): # 트리를 탐색하는 함수
    now=1
    while 1:
        if now>=20: return 0 # 배열범위 벗어나거나
        if arr[now]==0: return 0 # 해당 인덱스에 자식이 없거나
        if arr[now]==target: return 1 # 찾았으니 1리턴
        if arr[now] < target: now=now*2+1 # target값이 더 커서 우측 트리 확인
        else: # 왼쪽트리 확인
            now=now*2

for i in lst:
    Insert(i)


# 숫자 하나 입력받고.. 입력받은 숫자가 tree 에 존재하는지 출력
n=int(input())
ans=Search(n)
if ans: print("존재")
else: print("없는숫자")
