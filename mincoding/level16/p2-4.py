a, b= map(int,input().split())
lst = [a,b]

def multi(arr):
    if len(arr) < 6:
        arr.append(arr[-1] * arr[-2])
        multi(arr)
        return arr[-1]

result = multi(lst)
print(result)