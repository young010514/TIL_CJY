# DFS BackTracking !!
# : 모든 경우의 수를 다 봐야한다
# : 최소 이동

"""
(0,0)에서 출발 --> 몬스터 포획 --> 의뢰인에게 전달

손님 id: -1 ~ -4번 (음수)
몬스터 id: 1 ~ 4번 (양수)
--> idx: id, value: (x, y)

dist = |x1-x2| + |y1-y2|

Back Tracking
몬스터를 잡는 순서 ==> 모든 경우의 수를 다 봐야함 (DFS) ==> 최소 이동거리
1) 아직 몬스터를 잡지 않았다면 --> 사람한테 가면 안됨 (가지치기)
2) ret보다 지금까지의 이동거리가 더 크다면 (가지치기)
"""


def DFS(x, y, level, total_dist):  # (x, y, 몇번, 이동거리)
    global result

    # 1. 종료조건
    if level == target_cnt:  # 모두 방문 완료했으면 종료
        result = min(result, total_dist)

    # 2. 다음 고를거
    for i in target_lst:  # (x, y)에서 모든 타켓들까지의 거리 계산

        if target_info[i][0] == 1: continue # 방문한적 있으면 무시

        if i < 0 and target_info[-i][0] == 0: continue # 해당 노드가 사람(음수)인데, 목표 몬스터를 방문(포획)한적 없으면 무시

        # 방문한적 없는데 && (양수이거나 or 음수지만 해당 몬스터를 포획해놨다면)
        target_info[i][0] = 1  # 방문 처리
        dist = abs(x - target_info[i][1]) + abs(y - target_info[i][2])  # 거리 측정: dist = |x1-x2| + |y1-y2|
        DFS(target_info[i][1], target_info[i][2], level + 1, total_dist + dist)  # 함수 실행
        target_info[i][0] = 0  # 원상 복구


testcase = int(input())
for tc in range(1, testcase + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    target_lst = []  # 방문해야할 의뢰인 & 몬스터 리스트
    target_info = {}  # 타겟 정보 idx: 의뢰인 or 몬스터 No. |  value: [방문여부, y, x]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0: continue
            target_lst.append(arr[i][j])  # eg. [2, -1, ...]
            target_info[arr[i][j]] = [0, i, j]

    target_cnt = len(target_lst)
    result = 21e8

    DFS(0, 0, 0, 0)  # 시작좌표 /  level /  이동거리

    print(f'#{tc} {result}')