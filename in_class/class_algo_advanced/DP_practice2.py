arr=[
    [0,1,2,2],
    [1,3,4,1],
    [5,8,1,4],
    [9,1,78,0]]

result = [[5e5] * 4 for _ in range(4)]
result[0][0] = 0
def dp():
    global result
    for i in range(4):
        for j in range(4):
            for x in range(2):
                dx = i + (1-x)
                dy = j + x
                if dx >3 or dy >3 :continue
                if result[dx][dy] > result[i][j] + arr[dx][dy] :
                    result[dx][dy] = result[i][j] + arr[dx][dy]
dp()
print(result[3][3])

