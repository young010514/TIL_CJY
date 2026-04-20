arr = [
    list('GKG'),
    list(input())
]
dic = {}
for inner in arr:
    for x in inner:
        dic.setdefault(x,0)
        dic[x] += 1
result = '없음'
for i in dic.values():
    if i >= 3:
        result= '있음'
print(result)