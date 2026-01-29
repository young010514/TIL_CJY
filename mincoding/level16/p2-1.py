a,b,c = map(int,input().split())
for i in range(c):
    for x in range(a,b+1):
        print(x,end=' ')
    print()