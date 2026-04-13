levelTable = [
    [10,20],
    [30,60],
    [100,150],
    [200,300],
]
ip = list(map(int,input().split()))
result = [0,0,0,0]
for i,inner in enumerate(levelTable):
    for data in ip:
        if inner[0] <= data <= inner[1]:
            result[i] += 1
for i in range(4):
    print(f'lev{i}:{result[i]}')
    
