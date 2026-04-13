import sys
sys.stdin = open("input_pw.txt" ,"r")

# T = int(input())
for tc in range(1,11):
    a,b = input().split()
    st = list(b)
    bn = True
    while bn:
        bn = False
        for i in range(len(st) - 1):
            if st[i] == st[i+1]:
                bn = True
                del st[i]
                del st[i]
                break
    result = ''.join(st)
    print(f"#{tc} {result}")