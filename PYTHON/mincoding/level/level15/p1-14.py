arr = [
    list('POTIO'),
    list('ABCDE'),
    list('YOURE'),
]
a, b =map(int,input().split())
for inner in arr:
    for x in inner[a:b+1]:
        print(x,end='')