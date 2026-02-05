arr = list("BGTK")
top = int(input())
def abc(level,idx):
    print(arr[idx],end='')
    if level == top:
        return
    for i in range(4):
        abc(level+1, i)
abc(0,0)