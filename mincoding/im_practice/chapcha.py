import sys
sys.stdin = open("input_chapcha.txt","r")

T = int(input())
for tc in range(1,T+1):
    n,k = map(int,input().split())
    sample = list(map(int,input().split()))
    passcode = list(map(int,input().split()))
    result = 1
    spl = sample[:]
    for i in range(k):
        if passcode[i] not in spl :
            result = 0
            break
        n_idx = spl.index(passcode[i])
        spl = spl[n_idx+1:]
    print(f"#{tc} {result}")