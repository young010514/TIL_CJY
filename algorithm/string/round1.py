import sys
sys.stdin = open("input_round1.txt","r")

def find_st(num):
    result = 0
    # 가로
    for i in range(8):
        for j in range(9-num):
            if arr[i][j:j+num] ==  arr[i][j:j+num][::-1]:
                result += 1

    # 세로
    for j in range(8):
        for i in range(9-num):
            st1 = ''
            for d in range(num):
                st1 += arr[i+d][j]
            if st1 == st1[::-1]:
                result += 1
    return result

for t in range(10):
    n = int(input())
    arr = [list(input()) for _ in range(8)]
    ans = find_st(n)
    print(f"#{t+1} {ans}")


