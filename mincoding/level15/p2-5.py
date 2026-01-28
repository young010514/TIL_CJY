a, b, c = map(int,input().split())
for i in range(c):
    for x in range(a,a+b):
        print(x,end=' ')
    print()