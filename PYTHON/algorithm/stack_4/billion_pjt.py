import sys
sys.stdin = open("input_billionpjt.txt","r")

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    lst= list(map(int,input().split()))
    result =0
    while lst:
        max_data = max(lst)
        max_idx = lst.index(max_data)
        if max_idx == 0:
            lst.pop(0)
            continue
        max_sum = max_data * max_idx
        for i in range(max_idx):
            max_sum -= lst[i]
        result += max_sum
        lst = lst[max_idx+1 : ]


    print(f"#{tc} {result}")