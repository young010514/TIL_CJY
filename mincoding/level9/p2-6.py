arr = [[3,5,14], [2,3,9], [6,2,7]]
n = int(input())
cnt = 0
for inner in arr:
    for data in inner:
        if data % n == 0 :cnt += 1
print(cnt)