T = int(input())
for tc in range(1,T+1):
    a,b,c = map(int,input().split())
    def candy(a,b,c):
        result = 0
        if c <= 2 or b <= 1: return -1
        if b >= c :
            result += b-c+1
            b = c-1
        if b <= 1 : return -1
        if a >= b :
            result += a - b + 1
        return result
    result = candy(a,b,c)
    print(f"#{tc} {result}")

