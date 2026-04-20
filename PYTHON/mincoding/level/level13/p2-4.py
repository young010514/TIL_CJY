arr=[[3,4,1,6],[3,5,3,6],[0,0,0,0],[5,4,6,0]]
a = list(map(int,input().split()))
i = 0
for x in a:
    arr[2][i] = x
    i += 1
    
mx, mn = arr[0][0], arr[0][0]

for x,inner in enumerate(arr):
    for y,i in enumerate(inner):
        if i > mx : 
            mx = i
            mx_xy = (x,y)
        if i < mn:
            mn = i
            mn_xy = (x,y)
print(f'MAX={mx}({mx_xy[0]},{mx_xy[1]})')
print(f'MIN={mn}({mn_xy[0]},{mn_xy[1]})')