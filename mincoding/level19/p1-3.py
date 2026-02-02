lst = [
    ['_','_','_','_','_',],
    ['_','_','_','_','_',],
    ['_','_','_','_','_',],
    ['_','_','_','_','_',],
]
a,b= map(int,input().split())
c,d= map(int,input().split())
for x, y in [(a,b), (c,d)]:
    for i in [-1,1]:
        if 0 <= x+i < len(lst):
            lst[x+i][y] = "#"
        if 0 <= y+i < len(lst[0]):
            lst[x][y+i] = "#"
        if 0 <= y+i < len(lst[0]) and 0 <= x+i < len(lst):
            lst[x+i][y+i] = "#"
        if 0 <= y-i < len(lst[0]) and 0 <= x+i < len(lst):
            lst[x+i][y-i] = "#"
for inner in lst:
    print(' '.join(inner))