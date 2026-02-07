lst = ["A",'B','C']
cnt = 0
N = int(input())
def abc(level,st):
    global cnt
    if level == N:
        if "AAA" not in st and "BBB" not in st and "CCC" not in st: 
            cnt += 1
        return
    for i in range(len(lst)):
        abc(level+1, st + lst[i])
abc(0,"")
print(cnt)