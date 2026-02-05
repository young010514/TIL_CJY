
branch,level =map(int,input().split())
cnt = 0
def abc(a):
    global cnt
    cnt += 1
    if a == level :
        return
    for i in range(branch):
        abc(a+1)
abc(0)
print(cnt)

