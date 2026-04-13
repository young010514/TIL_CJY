level = int(input())
branch=int(input())

def abc(a):

    if a == level :
        return
    for i in range(branch):
        abc(a+1)
abc(0)

