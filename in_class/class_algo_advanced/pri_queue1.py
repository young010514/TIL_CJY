import heapq
# min heap 이 기본값

# 배열 입력 받은 후
# 1. 짝수 우선
# 2. 내림차순 (큰숫자 우선 출력)

arr = [3,4,1,8,7,2,5,6]
# 정답 : 8,6,4,2,7,5,3,1


arr = [3,4,1,8,7,2,5,6]
heap = []
# 비추 : 시간복잡도 NlogN
# for i in range(len(arr)):
#     priority = (arr[i] % 2 , -arr[i])       # 조건 명시 / 튜플로 명시하고, 앞에꺼부터 한 다음 뒤에것 정렬
#     heapq.heappush(heap,(priority,arr[i]))
for i in range(len(heap)):
    print(heapq.heappop(heap)[1],end=' ')

# 추천 !  heapify 활용 => 시간 복잡도 N
heap2 = [((i%2, -i), i) for i in arr]
heapq.heapify(heap2)

while heap2 :
    _, value = heapq.heappop(heap2)
    print(value,end=' ')