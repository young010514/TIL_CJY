n = int(input())
def p_num(num):
    print(abs(num), end=' ')
    if num > -n :
        p_num(num-1)
    else:
        return
p_num(n)