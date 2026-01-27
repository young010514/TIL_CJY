arr = list(map(int,input().split()))
arr1 = [arr[:3], arr[3:]]
for inner in arr1:
    for i in inner:
        if i == 0 :
            print("#",end='')
        else:print(i,end='')
    print()
