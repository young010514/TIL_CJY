import sys
sys.stdin = open("input_truck.txt","r")


# bfs 로 풀기
def main(lst):
    global result,n,arr
    if result < len(lst):
        result = len(lst)
    for i in range(n):
        if lst[-1][1] <= arr[i][0]:
            lst.append(arr[i])
            main(lst)
            lst.pop()



T = int(input())
for tc in range(1,T+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    arr.sort()
    result = 0
    for i in range(n):
        main([arr[i]])
    print(f"#{tc} {result}")