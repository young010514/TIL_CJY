n = int(input())
cnt = 0
Sum = 0
def abc(level):
    global cnt,Sum
    if level == n-1:
        cnt += 1
        return
    for i in range(8):
        Sum += i
        if Sum <= 7:
            abc(level + 1)
        Sum -= i
abc(0)
print(cnt)
