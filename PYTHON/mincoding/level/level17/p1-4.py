arr =[
    list("ATKB"),
    list("CZFD"),
    list("HGEI"),
]
a,b,c = input().split()
for i in range(3):
    for j in range(4):
        if arr[i][j] == a:
            x,y = i+int(b), j+int(c)

print(arr[x][y])