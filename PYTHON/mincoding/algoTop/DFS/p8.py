def findup(x):
    if arr[x] == 0:
        return x
    ret = findup(arr[x])
    arr[x] = ret
    return ret
def win(a,b):
    upa = findup(a)
    upb = findup(b)
    if upa == upb : return

    arr[upb] = upa
u,v,x = map(int,input().split())
arr = [0] * (u+1)
for _ in range(v):
    a,b = map(int,input().split())
    win(a,b)
print(arr)
# 최소 등수 출력
if arr[x] == 0 : print("1")
else:
    cnt= arr.count(findup(x))
    print(cnt + 1)
print(u-arr.count(x))