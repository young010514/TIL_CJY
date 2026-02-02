import sys
sys.stdin = open("input.txt", "r")

for t in range(10):
    n = int(input())
    lst = list(map(int,input().split()))
    for i in range(n):
        for d in range(1, 3):
            if lst[i+d] > lst[i]
