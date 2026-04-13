vect = [[3,7,4],[2,2,4],[2,2,5]]
target = list(map(int,input().split()))
result = [0,0,0]

for i in range(3):
    result[i] += vect[i].count(target[i])

print(target[result.index(max(result))])