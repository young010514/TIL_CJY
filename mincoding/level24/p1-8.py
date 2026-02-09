s = input()
a,b,c = map(int,input().split())
for _ in range(c):
    for i in range(a,b+1):
        print(s[i], end='')
