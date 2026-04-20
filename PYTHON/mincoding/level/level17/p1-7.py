arr1 = [
    [0,0,1,0,0],
    [0,0,1,1,1],
]
arr2 = [
    [3,5,4,1,1],
    [3,5,2,5,6]
]
num = int(input())
result =0
for i in range(2):
    for j in range(5):
        if arr1[i][j] and arr2[i][j] == num :
            result = 1
if result:
    print(f'{num} 존재')

else:
    print(f'{num} 없음')