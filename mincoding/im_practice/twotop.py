import sys
sys.stdin = open("input_twotop.txt","r")

T = int(input())
for tc in range(1,T+1):
    n,m1,m2 = map(int,input().split())
    lst = list(map(int,input().split()))
    used=[0] * n
    lst1, lst2 = [],[]
    lst.sort(reverse=True)
    m = min(m1,m2)
    for i in range(m):
        lst1.append(lst[2*i])
        lst2.append(lst[2*i+1])
    lst2.extend(lst[2*m:])
    result =0
    for i in range(m):
        result += (i+1) * lst1[i]
    for i in range(n-m):
        result += (i+1) * lst2[i]

    print(f"#{tc} {result}")