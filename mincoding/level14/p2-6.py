def main():
    arr= [[0,0,0],[0,0,0],[0,0,0]]
    arr1 = Magic(arr)
    output(arr1)
def Magic (arr):
    n = 1
    for i in range(3):
        for j in range(i,3):
            arr[i][j] = n
            n += 1
    return arr
def output(arr):
    for inner in arr:
        for x in inner:
            if x :print(x,end='')
            else:print(' ',end='')
        print()
main()