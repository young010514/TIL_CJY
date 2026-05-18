import sys
sys.stdin = open("input/in_1256.txt","r")

T = int(input())
for tc in range(1,T+1):
    k = int(input())
    st = input()
    arr = []
    for i in range(len(st)):
        arr.append(st[i:])
    arr.sort()
    print(f"#{tc} {arr[k-1]}")

