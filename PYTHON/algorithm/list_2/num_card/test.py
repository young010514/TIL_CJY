import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(T):
    n = int(input())
    lst = list(map(int,list(input())))
    new_dic = {}
    for x in lst:
        if new_dic.get(x):
            new_dic[x] += 1
        else: new_dic[x] =1

    x,y = lst[0], 1

    for a,b in new_dic.items():
        if b > y:
            x, y = a, b
        elif b == y and a > x: x= a
    print(f'#{t+1} {x} {y}')
