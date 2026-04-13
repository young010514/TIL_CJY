# Dijkstra : "최소비용" algo

# 개선 전 다익스트라
name ="ABCDE"
inf = int(21e8)
arr = [
    [0,3,inf,9,5],
    [inf,0,7,inf,1],
    [inf,inf,0,1,inf],
    [inf,inf,inf,0,inf],
    [inf,inf,1,inf,0],
]

result = [inf] * 5
used =[0]* 5

# 0번 인덱스 (시작점을 첫 경유지로 놓기)
used[0] =1
result[0]=0

def select_ky():
    Min = int(21e8)
    Min_index = 0
    for i in range(5):
        if used[i] == 0 and result[i] < Min :
            Min = result[i]
            Min_index = i
    return Min_index

def dijkstra():
    # 경유지 선택
    for i in range(5):
        via = select_ky()
        used[via] = 1

    # 바로 가는 것과 경유지 통과 시 더 작은 값을 result 에 갱신
        for j in range(5):
            baro = result[j]
            kyung = result[via] + arr[via][j]
            if baro > kyung : result[j] = kyung

dijkstra()
print(result)



