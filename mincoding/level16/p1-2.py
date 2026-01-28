arr = [
    list("ABKT"),
    list("KFCF"),
    list("BBQQ"),
    list("TPZF"),
]
a, b= input().split()
cnt = 0
for inner in arr:
    cnt += inner.count(a)
    cnt += inner.count(b)
print(cnt)