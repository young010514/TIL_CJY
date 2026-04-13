# TopDown
def fibo(n):

    if n <= 1 :
        return memo[n]
    if memo[n] != -1 :
        return memo[n]

    memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n]


memo = [-1] * 5
memo[0], memo[1] = 0,1
fibo(4)
print(memo)

# Bottomup

def fibo(n):
    global dp
    for i in range(2,n+1):
        dp[i]=dp[i-2]+dp[i-1]

dp=[0]*5
dp[0]=0
dp[1]=1

fibo(4)
print(dp)
