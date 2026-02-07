lst = list(input())
cnt = 0
def abc(level,st):
    global cnt
    if level == 4:
        if "BT" not in st and "TB" not in st: 
            cnt += 1
        return
    for i in range(len(lst)):
        abc(level+1, st + lst[i])
abc(0,"")
print(cnt)