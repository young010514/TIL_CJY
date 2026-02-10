import sys
sys.stdin = open("input_find.txt", "r")

for _ in range(10):
    tc, n = map(int,input().split())

    in_lst = list(map(int,input().split()))

    lst1 = [[] for _ in range(100)]

    for i in range(n):
        lst1[in_lst[2*i]].append(in_lst[2*i+1])

    result =0
    def find(idx):
        global result
        if lst1[idx] == []:
            return
        if 99 in lst1[idx]:
            result = 1
            return
        for i in lst1[idx]:
            find(i)
    find(0)
    print(f"#{tc} {result}")