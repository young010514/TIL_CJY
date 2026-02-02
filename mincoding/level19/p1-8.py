image = []
for i in range(4):
    image.append(list(map(int,input().split())))
def rectSum(x,y) :
    result = 0
    for i in range(2):
        for j in range(3):
            result+= image[x+i][y+j]
    return result
data = rectSum(0,0)
for x in range(3):
    for y in range(2):
        if data < rectSum(x,y):
            data = rectSum(x,y)
            idx = x,y
print(f"({idx[0]},{idx[1]})")