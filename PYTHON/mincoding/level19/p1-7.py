vect =[
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [0,0,0],
]

for i in range(4):
    x,y = map(int,input().split())
    vect[x][y] = 5
for inner in vect:
    print(*inner)