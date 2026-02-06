arr = list("BGTK")
top = int(input())
def abc(level,st1):
    if level == top:
        print(st1,)
        return
    for i in range(4):
        abc(level+1, st1 + arr[i])
abc(0,"")