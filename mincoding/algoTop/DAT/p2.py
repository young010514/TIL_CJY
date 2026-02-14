vect = "MINCODING"
n = int(input())
lst = input().split()
for i in lst:
    if i in vect : print("O",end='')
    else:print("X",end='')