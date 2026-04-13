import sys
sys.stdin = open("input_bus.txt","r")

T = int(input())
for t in range(T):
    result, ans = {},[]
    n = int(input())
    for _ in range(n):
        x,y= map(int,input().split())
        for i in range(x,y+1):
            if result.get(i):
                result[i] += 1
            else:result[i] = 1

    p = int(input())
    for _ in range(p):
        num = int(input())
        if result.get(num):
            ans.append(result[num])
        else:ans.append(0)
    print(f"#{t+1}", *ans)