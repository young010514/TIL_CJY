import sys
sys.stdin = open("input.txt", "r")

for t in range(10):
    n = int(input())
    lst = list(map(int,input().split()))
    result = 0
    for i in range(n):
        bool_data = True
        data = lst[i]
        for d in range(-2,3):
            if d != 0 and 0 <= i+d < n:
                if lst[i+d] >= lst[i]:
                    bool_data = False
                elif data > lst[i] - lst[i+d]:
                    data = lst[i] - lst[i+d]
        if bool_data:
            result += data
    print(f"#{t+1} {result}")
