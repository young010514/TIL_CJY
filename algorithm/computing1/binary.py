import sys
sys.stdin = open("input_binary.txt","r")

T = int(input())
for tc in range(1,T+1):
    a,b = input().split()
    a = int(a)
    lst = list(b)
    jin = list(map(str,list(range(10)))) + list("ABCDEF")
    num = 0
    def to_binary(value):
        num = jin.index(value)
        result = list("0000")
        i = 0
        while num :
            result[-i-1] = str(num % 2)
            num //=2
            i +=1

        return ''.join(result)
    ans = ''
    for i in lst:
        ans += to_binary(i)
    print(f"#{tc} {ans}")