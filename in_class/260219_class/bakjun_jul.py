n,m = map(int,input().split())

# 편의상 0번 학생은 없으니 필요한 값들을 받는 리스트의 길이를 모두 n+1로 설정함
acc = [0] * (n+1)
# 이때 to list의 경우는 뒤에 서야할 학생들을 추가
# 형식 : to[x] = [x 뒤에 서야할 친구들 리스트]
to = [[] for _ in range(n+1)]   # 인접리스트 형식으로
used = [0] * (n+1)

for _ in range(m):
    # 입력받기
    a,b = map(int,input().split())
    # acc 리스트에 1 추가
    acc[b] += 1
    # to list에 앞에 서야할 인덱스 추가
    to[a] += [b]

from collections import deque

q = deque()
# 0 부터 시작하면 안되니까, 1부터
for i in range(1,n+1):
    if acc[i] == 0 :
        # used 갱신해주고 append
        used[i] =1
        q.append(i)
while q:
    x = q.popleft()
    print(x,end=' ')
    # x 뒤에 설 친구가 있는 경우에만
    if to[x] :
        for i in to[x]:
            # acc 값이 1이고, 사용되지 않은 경우만
            if acc[i] == 1 and used[i] ==0:
                q.append(i)
                acc[i] -=1
                used[i] =1
            # 2 이상일 경우는 -= 만
            acc[i] -= 1
