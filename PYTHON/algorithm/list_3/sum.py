import sys
sys.stdin = open("input_sum.txt","r")

for q in range(10):
    t = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]

    max_data = -21e10

    right_point, left_point= 0,0

    for i in range(100):
        data1, data2 = 0,0
        for d in range(100):
            data1 += arr[i][d]
            data2 += arr[d][i]
        max_data = max([data1,data2,max_data])

        left_point += arr[i][i]
        right_point += arr[i][-i-1]
    max_data = max([max_data, left_point, right_point])
    print(f"#{t} {max_data}")