map1 = [
    [3,3,5,3,1],
    [2,2,4,2,6],
    [4,9,2,3,4],
    [1,1,1,1,1],
    [3,3,5,9,2],
]
max_data = map1[0][0]
for x,inner in enumerate(map1):
    for y, data in enumerate(inner):
        result = 0
        for i, j in [(-1,-1),(-1,1),(1,-1),(1,1)]:
            if 0 <= x + i < len(map1) and 0 <= y + j < len(map1):
                result += map1[x+i][y+j]
        if result > max_data:
            max_data = result
            final = [x,y]

print(f'{final[0]} {final[1]}')