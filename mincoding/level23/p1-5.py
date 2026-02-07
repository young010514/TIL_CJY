lst = ['E','W','A','B','C']
cnt = 0
N = input()
def abc(level,st):
    global cnt
    if level == 4:
        if N not in st: 
            print(st)
        return
    for i in range(len(lst)):
        if lst[i] not in st : abc(level+1, st + lst[i])
abc(0,"")