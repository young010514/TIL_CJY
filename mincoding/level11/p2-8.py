arr = [[3,1,6],[7,8,4],[9,2,3]]

a, b,c = map(int,input().split())
arr[a][b] = c
mx,mi = arr[0][0], arr[0][0]
for inner in arr:
    if mx < max(inner): mx = max(inner)
    if mi > min(inner): mi = min(inner)
print(mx+mi)