cardlist = list(input())
dic = {}
for x in cardlist:
    dic.setdefault(x,0)
    dic[x] += 1
# 비교할 값 초기화
data =0
ky = ''
for k,v in dic.items():
    if v > data:
        ky,data = k,v
print(ky)