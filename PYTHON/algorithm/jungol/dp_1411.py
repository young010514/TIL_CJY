n = int(input())

result = [0] * (n+1)
def dp():
    temp1, temp2 = 1, 1
    for i in range(2,n+1):
        ans = temp1*2 + temp2
        temp1 =temp2
        temp2= ans
    return ans
ans=dp()
print(ans %20100529)