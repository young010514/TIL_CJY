import sys
sys.stdin = open("input_repeat.txt" ,"r")

T = int(input())
for tc in range(1,T+1):
    st = list(input())
    bn = True
    while bn:
        bn = False
        for i in range(len(st) - 1):
            if st[i] == st[i+1]:
                bn = True
                del st[i]
                del st[i]
                break

    print(f"#{tc} {len(st)}")