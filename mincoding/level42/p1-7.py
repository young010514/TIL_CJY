name = list('abcdefg')
price = [15,20,44,22,55,16,45,]

st = input()
n = int(input())
used = [0] * len(st)

raw_sum = 0
for i in list(st):
    raw_sum += price[name.index(i)]
Max = 0


def dfs(level, Sum) :
    global Max
    if level == n:
        if Sum % 10 == 0 and Max < Sum:
            Max = Sum
        return
    for i in range(len(st)):
        if used[i]  == 0:
            used[i] = 1
            Sum -= price[name.index(st[i])]
            dfs(level +1, Sum )
            Sum += price[name.index(st[i])]
            used[i] = 0
dfs(0,raw_sum)
print(Max)