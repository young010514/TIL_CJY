lst = list(input())
cnt = 0
N = input()

def abc(level,st):
    global cnt
    if level == 4:
        if len(st) == 4: 
            cnt += 1
        return
    for i in range(len(lst)):
        if st and abs(int(st[-1]) - int(lst[i])) <=3:
            abc(level+1, st + lst[i])
        elif st == "": abc(level + 1, st + lst[i])
abc(0,"")
print(cnt)