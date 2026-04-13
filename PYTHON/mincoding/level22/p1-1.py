# branch = 3
# level =2

def abc(level,branch):
    if level == 2:
        print(chr(ord("A")+branch))
        return
    for i in range(3):
        if level ==1:
            print(chr(ord("A")+branch), end= '')
        abc(level+1, i)
abc(0,0)