n =int(input())
def fibo(level):
    if level == 1:
        return 0
    if level == 2:
        return 1
    return fibo(level-1) + fibo(level-2)
print(fibo(n))