T = int(input())
for t in range(T):
    n,m = map(int,input().split())
    lst_n = list(map(int,input().split()))
    lst_m = list(map(int,input().split()))
    if n > m :
        lst1, lst2 = lst_n[:], lst_m[:]
        l,s = n,m
    else:
        lst1, lst2 = lst_m[:], lst_n[:]
        l,s=m,n
    max_data = -21e20
    for d in range(l-s+1):
        data = 0
        for i in range(s):
            data += lst1[d+i] * lst2[i]
        if data > max_data :
            max_data = data
    print(f'#{t+1} {max_data}')

