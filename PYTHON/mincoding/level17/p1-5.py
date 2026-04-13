arr = [
    [3,5,9],
    [4,2,1],
    [5,1,5],
]
ip = list(map(int,input().split()))
result =['미발견','미발견','미발견']
for inner in arr:
    for i in range(3):
        if ip[i] in inner : result[i] ='존재'
for i in range(3) :
    print(f'{ip[i]}:{result[i]}')