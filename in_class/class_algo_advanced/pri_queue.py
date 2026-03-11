# 우선순위 큐

# 큐 - FIFO
# 우선순위 - 데이터의 우선순위가 정해졌을 때, 그 우선순위에 의거해서 우선순위가 높은 데이터를 먼저 꺼내서 사용할 때 사용하는 큐

# import heapq                  # 주로 이거 활용할 예정!
# from queue import PriorityQueue # heapq 보다 연산속도가 더 느림 / 알고리즘 문제 풀이시 부적합


# heapq 사용법
# 1. 입력되는 값을 우선순위 큐에 넣고 출력해보기1
import heapq
arr = []
heapq.heappush(arr,4)       # 우선순위 큐의 규칙에 의거해서 데이터 저장
heapq.heappush(arr,1)       # min heap이 기본적으로 저장
heapq.heappush(arr,3)
heapq.heappush(arr,6)
heapq.heappush(arr,9)
print(arr)
# print(heapq.heappop(arr))
# print(heapq.heappop(arr))
# print(heapq.heappop(arr))
# print(heapq.heappop(arr))
# for i in range(len(arr)):print(heapq.heappop(arr),end=' ')

# while arr:
#     node = heapq.heappop(arr)
#     print(node,end=' ')

# ========================================================
# 2. 배열을 우선순위 큐로 바꿔보기
import heapq
arr = [3422,5,3,1,5]
heap = []
# 기존 배열을 for 문으로 우선순위 큐에 저장하고, 우선순위 큐를 출력해볼 수 있다.
for i in range(len(arr)):
    heapq.heappush(heap,arr[i])
for i in range(len(arr)):
    print(heapq.heappop(heap),end=' ')

# ==================================================
# 방법2. heapify를 이용해서 한번에 heap의 자료구조 변환
import heapq
arr = [3422,5,3,1,5]
heapq.heapify(arr)
for i in range(len(arr)):
    print(heapq.heappop(arr))


# ================================================================
# Max heap 으로 출력해보기
import heapq
arr = [3422,5,3,1,5]
heap = []
for i in range(len(arr)):
    heapq.heappush(heap,-arr[i])
print(heap)
# max heap을 기본으로 저ㅔ공해주는 메소드가 없으므로 pop 할때 -1 곱해서 할 것
for i in range(len(arr)):
    # print(heapq.heappop(heap) * -1,end=' ')
    print(-heapq.heappop(heap),end=' ')

# Max heap으로 출력해보기 (방법2)
import heapq
arr = [3422,5,3,1,5]
heap = []
for i in range(len(arr)):
    heapq.heappush(heap, (-arr[i],arr[i]))
print(heap)
for i in range(len(arr)):
    print(heapq.heappop(heap)[1],end=' ')
    print(heap)
# Max heap으로 출력해보기 방법 3
# heapify 사용
import heapq
arr = [3422,5,3,1,5]
arr = list(map(lambda x : -x, arr))
heapq.heapify(arr)
print(arr)






















