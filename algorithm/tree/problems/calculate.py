import sys
sys.stdin =open("input_calcul.txt","r")

def cal(idx):
    now = lst[idx]
    ndata = now[1]
    if ndata.isdigit(): return int(ndata)
    else:
        left, right =int(now[2]),int(now[3])
        if ndata == "+" : return cal(left) + cal(right)
        elif ndata == "-" : return cal(left) - cal(right)
        elif ndata == "*" : return cal(left) * cal(right)
        elif ndata == "/" : return cal(left) / cal(right)

for tc in range(1,11):
    n = int(input())
    lst = [0] + [input().split() for _ in range(n)]
    #print(lst)
    result = cal(1)
    print(f"#{tc} {int(result)}")