# Stack (Last In First Out)
# list .append, .pop 과 동일
st = list()
st.append(3)
st.append(4)
st.append(5)
st.append(6)
print(st)
st.pop()
st.pop()
st.pop()
print(st)


# Queue (First In First Out)
# list .append, .pop(0) 과 동일
# .pop()은 시간 복잡도가 O(1) 이지만
# .pop(0)는 시간 복잡도가 O(N) 이라 파이썬에서 활용하지 않음

from collections import deque
# collection module 내에 deque 클래스 활용 => O(1)의 속도로 .pop(0)을 할 수 있음

q = deque()
q.append(5)
q.append(6)
q.append(7)
q.append(8)
q.append(9)
print(q)        # deque([5, 6, 7, 8, 9])
# * 사용해서 deque 클래스 안의 값을 빼온 다음 []로 감싸면 리스트 형식으로 출력 가능
print([*q])     # [5, 6, 7, 8, 9]

# .pop(0) 와 동일한 방식
q.popleft()
q.popleft()
print([*q])     # O(1) 의 시간 복잡도를 갖고 삭제 가능
q.pop()
print([*q])

# 이는 보통 BFS 구현 할 때 많이 활용함
# Queue FIFO
# 참고
import BFS
q= BFS.Queue()
q.put(1)    # q.append()
q.put(2)
q.put(3)
q.get()     # q.pop(0) or q.popleft()
print(q)
print(list(q.queue))    # 리스트 형식을 출력 가능
