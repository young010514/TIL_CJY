import sys
sys.stdin = open("input_round.txt", "r")

for tc in range(1,11):
    n = int(input())

    # 이진트리로 만들기
    left = [0] * (n+1)
    right = [0] * (n+1)
    par = [0] * (n+1)
    data =[0] * (n+1)
    for i in range(n):
        lst = input().split()
        idx = int(lst[0])
        data[idx] = lst[1]
        if len(lst) >= 3:
            left[idx]= int(lst[2])
        if len(lst) == 4:
            right[idx]= int(lst[3])
    print(f"#{tc}",end=' ')
    def in_order(T):
        if T:
            in_order(left[T])
            print(data[T],end='')
            in_order(right[T])

    in_order(1)
    print()