import sys
sys.stdin = open("input.txt","r")

T = int(input())


for _ in range(T):
    t, n = input().split()
    lst = input().split()

    to_sort_lst = [
        "ZRO",
        "ONE",
        "TWO",
        "THR",
        "FOR",
        "FIV",
        "SIX",
        "SVN",
        "EGT",
        "NIN",
    ]
    result = {
        0 :0,
        1:0,
        2:0,
        3:0,
        4:0,
        5:0,
        6:0,
        7:0,
        8:0,
        9:0,
    }

    for i in lst:
        result[to_sort_lst.index(i)] += 1

    print(t)
    for i in to_sort_lst:
        for d in range(result[to_sort_lst.index(i)]):
            print(i, end=' ')

