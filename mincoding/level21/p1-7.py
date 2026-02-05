st = input()
def abc(level):
    print(level,end=' ')
    if level ==1:
        return
    abc(level-1)
    print(level,end=' ')

abc(len(st))