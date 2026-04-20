lst = list(input())
def abc(level,st):
    if level == 3:
        if len(st) == 3: 
            print(st)
        return
    for i in range(len(lst)):
        if lst[i] not in st : abc(level+1, st + lst[i])
        else:abc(level+1, st)
abc(0,"")