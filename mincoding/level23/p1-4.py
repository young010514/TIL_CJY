lst = ['B','T','S','K','R']
cnt = 0
N = int(input())
def abc(level,st):
    global cnt
    if level == N:
        if len(set(list(st))) == N and "S" in st: 
            cnt += 1
        return
    for i in range(len(lst)):
        abc(level+1, st + lst[i])
abc(0,"")
print(cnt)