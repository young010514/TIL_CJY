arr = [input() for _ in range(5)]
cnt = 0
for i in arr:
    # print(i.count("MCD"))
    cnt += i.count("MCD")
print(cnt)