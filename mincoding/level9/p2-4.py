arr = [[10,3,20], [60,30,40], [20,30,40]]
a, b= map(int,input().split())
cnt = 0
for inner in arr:
    for data in inner:
        if a <= data <= b: cnt+=1
print(cnt)