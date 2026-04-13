lst = list(map(int,list(input())))
cnt = 0
# N = input()

def abc(level,st):
    global cnt
    if level == 4:
        if len(str(st)) == 4: 
            cnt += 1
        return
    for i in range(len(lst)):
        if level == 0: abc(level+1, st + lst[i])
        elif -3<= st%10 - lst[i] <=3:
            abc(level+1, 10 * st + lst[i])
abc(0,0)
print(cnt)