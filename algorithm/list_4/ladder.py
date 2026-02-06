import sys
sys.stdin = open("input_ladder2.txt","r")

def find_point(y):
    x=0
    while True:
        if x == len(arr)-1 :
            return y
            break
        # index error 방지를 위해 y+1 또는 y-1이 index를 넘어가지 않는지 먼저 확인
        if y + 1 < len(arr[0]) and arr[x][y + 1] == 1:
            while y <len(arr[0]) and arr[x][y] == 1:
                y += 1
            y -= 1

        elif y > 0 and arr[x][y-1] == 1:
            while y >= 0 and arr[x][y] == 1 :
                y-=1
            y += 1

        # 오른쪽이나 왼쪽으로 이동하거나, 아래로 이동하는건 항상 default
        x += 1

for _ in range(10):
    t = int(input())
    arr= [list(map(int,input().split())) for _ in range(100)]
    for i in range(len(arr[0])):
        if arr[0][i]==1:
            b = find_point(i)
            if arr[len(arr)-1][b] == 2 :
                result = i
                break
    print(f"#{t} {result}")

