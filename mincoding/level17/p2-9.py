arr = list(map(int,input().split()))
print(f'arr[{arr.index(min(arr[::2]))}]={min(arr[::2])}')