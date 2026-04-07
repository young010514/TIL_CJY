n = int(input())
def fibo(num):
    arr = [0] * (num+1)
    arr[0], arr[1] = 0,1
    for i in range(2,num+1):
        arr[i] = arr[i-1] + arr[i-2]

    return arr[num]
print(fibo(n)%(1000000007))