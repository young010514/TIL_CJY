arr = [[3,5,9],[4,2,1],[1,1,5]]
ox = []


for i in range(3):
    a1 = list(map(int,input().split()))
    ox.append(a1)

result = 0
for i in range(3):
    for j in range(3):
        result += arr[i][j] * ox[i][j]
print(result)