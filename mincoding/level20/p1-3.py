lst = list(map(int,input().split()))
def p_arr(i):
    if i < len(lst):
        print(lst[i], end=' ')
    elif i < len(lst) * 2 - 1:
        print(lst[len(lst)-i-2], end=' ')
    else: return
    p_arr(i+1)
p_arr(0)