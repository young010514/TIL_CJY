arr = [10,50,40,20,30,40]
arr1= list(map(int,input().split()))
for a in arr1:
    cnt =0
    for b in arr:
        if a < b :cnt +=1
    print(f"{a}={cnt}개")