lst = [[3,1,9],[7,2,1],[1,0,8]]
bit = []
for i in range(3):
    bit.append(list(map(int,input().split())))

result = '미발견'
for x,inner in enumerate(bit):
    for y,i in enumerate(inner):
        if i and 3 <= lst[x][y] <=5 :
            result = '발견'
print(result)