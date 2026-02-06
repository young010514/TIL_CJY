import sys
sys.stdin = open("input_count.txt", "r")

T = int(input())
for t in range(T):
    str1= list(input().strip())
    str2 = list(input().strip())

    result = [0]*1000
    for idx, i in enumerate(str1):
        result[idx] = str2.count(i)

    print(f"#{t+1} {max(result)}")