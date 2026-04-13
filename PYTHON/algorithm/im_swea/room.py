n,k = map(int,input().split())
lst = [tuple(map(int,input().split())) for _ in range(n)]
data = {}
for i in lst:
    if data.get(i) : data[i] +=1
    else: data[i] = 1
result = 0
for v in data.values():
    if v % k == 0 :
        result += v//k
    else:result += v//k + 1
print(result)