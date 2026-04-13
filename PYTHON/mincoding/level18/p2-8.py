lst = [list(input()) for _ in range(3)]
result = [0] * 200
for i in lst:
    for x in i:
        result[ord(x)] += 1
if sum(result) > result.count(1): print("No")
else:print("Perfect")