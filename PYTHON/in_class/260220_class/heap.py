# Max heap 구현

arr= [6,4,2,34,6,5,3,2,43]
heap = [0]*20   # 여유있게 20칸 리스트 선언
hindex = 1 # 루트노드는 1번 인덱스 부터 시작하니까

def Insert(value):  # 이진트리 형태로 저장하는 함수
    global hindex
    heap[hindex] = value    # 넘어온 값 heap list에 저장
    now = hindex    # 넘어온 값이 저장된 index가 곧 now
    hindex +=1
    while 1:
        p = now // 2
        if p ==0 : break # 지금 현재 루트노드라면 부모랑 비교 불가하므로 break
        if heap[p] >= heap[now] : break     # 부모값이 더 크면 break
        heap[p],heap[now]=heap[now],heap[p] # 자식이 더 크면 swap
        now = p                             # 이후 부모의 부모랑 또 비교하기 위해 now 갱신
def Top() :  # 출력하는 함수
    return heap[1]
def Pop():      # 출력된 값을 빼고, 맨 뒤에 값 올린 다음 필요시 swap
    global  hindex
    hindex -= 1     # 가장 뒤에 있는 값을 가르키기
    heap[1] = heap[hindex]  # 가장 뒤에 값 맨앞으로 옮기고
    heap[hindex] = 0    # 맨뒤의 값 제거

    # 1. 두 자식을 비교 : 오른쪽 자식이 존재하고 and 오른쪽 자식이 왼쪽 자식보다 크면
    # 2. 자식이 없거나 or 자식이 부모보다 더 작으면 break

    now = 1
    while 1:
        son = now*2
        rson = now*2+1
        if rson < hindex and heap[son] < heap[rson] : son = rson    # 주석 1
        if son >= hindex or heap[now] > heap[son] : break          # 주석 2
        heap[now], heap[son] = heap[son],heap[now]
        now=son
for i in range(len(arr)):
    Insert(arr[i])
for i in range(len(arr)):
    print(Top(),end=' ')    # 출력
    Pop()   # 값 제거