import sys
sys.stdin = open("input_waterbbu.txt","r")


T = int(input())
for tc in range(1,T+1):
    n = int(input())
    lst = list(map(int,input().split()))
    Max = max(lst)
    data = []
    for i in lst:
        data.append(i-Max)

    def dfs(level):
        if sum(data) == 0 :
            return level
        for i in range(n):
            if data[i] == 0 :continue
            if data[i] + level%2 >0 : continue


    result = dfs(1)
    print(result)