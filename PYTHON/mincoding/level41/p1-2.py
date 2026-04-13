n = int(input())
lst = list(map(int,input().split())) + [0] * 10
now_loc = 0
result = -21e10
def mario(loc,score):
    global  result
    if loc > n:
        if result < score:
            result = score
        return

    for i in [2,7]:
        mario(loc + i, score + lst[loc + i])


mario(-1,0)
print(result)
