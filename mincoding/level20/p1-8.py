def abc(num):
    if num ==0:
        return
    abc(num // 2)
    print(num,end=' ')
n = int(input())
abc(n)