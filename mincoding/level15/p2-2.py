arr=[
    [5,1,4,2,6],
    [3,5,0,0,7],
    [9,9,8,3,1],
]
num = int(input())
cnt =0
for inner in arr:
    for x in inner:
        if x > num:
            cnt+=1
print(f"{cnt}개")