import sys
sys.stdin = open('input/in_1266.txt','r')


def comb(n, k):
    if k > n:
        return 0
    k = min(k, n - k)  # 대칭성 활용

    res = 1
    for i in range(1, k + 1):
        res = res * (n - i + 1) // i
    return res

def main(x): # 소수가 아닐 확률 구하기
    

    
    # 소수 : 2,3,5,7,11,13,17
    arr = [2,3,5,7,11,13,17]
    ans = 0
    for i in range(19):
        if i in arr : continue
        ans += comb(18,i) * (x ** i) *((1-x) **(18-i))
    return ans



T = int(input())
for tc in range(1,T+1):
    a,b = map(int,input().split())
    # 둘다 소수가 아닐 확률을 구해서 빼기
    ans = 1- main(a/100) * main(b/100)
    print(f'#{tc} {ans:.6f}')