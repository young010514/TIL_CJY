import sys
sys.stdin = open("input/in_7465.txt","r")

def findboss(node):
    if arr[node] == 0:
        return node
    else:
        arr[node] = findboss(arr[node])
        return findboss(arr[node])

def union(a,b):
    fa = findboss(a)
    fb = findboss(b)
    if fa == fb : return
    arr[fa] = fb

T = int(input())
for tc in range(1,T+1):
    n,m = map(int,input().split())
    arr= [0] * (n+1)
    for _ in range(m):
        a,b= map(int,input().split())
        union(a,b)
    ans = arr.count(0)
    print(f'#{tc } {ans-1}')

