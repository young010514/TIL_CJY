arr= list(map(int,input().split()))
arr.sort(reverse=True)
[print(x,end='') for x in arr]