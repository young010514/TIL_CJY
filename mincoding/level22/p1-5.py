n = int(input())
def abc(level,st1):
    if level == 4:
        for x in st1:
            print(x,end='')
        print()
        return
    for i in range(1,n+1):
        st1.append(i)
        abc(level+1, st1)
        st1.pop()
abc(0,[])