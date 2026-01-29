arr = list(map(int,input().split()))
arr2 = [arr[:3], arr[3:]]

def max_find(lst):
    data = lst[0][0]
    result = 0,0
    for i in range(len(lst)):
        for j in range(len(lst[0])):
            if lst[i][j] > data :
                data = lst[i][j]
                result= i,j

    return f'({result[0]},{result[1]})'

def min_find(lst):
    data = lst[0][0]
    result = 0,0
    for i in range(len(lst)):
        for j in range(len(lst[0])):
            if lst[i][j] < data :
                data = lst[i][j]
                result= i,j

    return f'({result[0]},{result[1]})'
print(max_find(arr2))
print(min_find(arr2))