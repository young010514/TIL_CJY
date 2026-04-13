arr = [3,7,4,1,9,4,6,2]
def abc(idx):
    if idx == 0:
        print(arr[idx],end=' ')
        return
    print(arr[idx],end= ' ')
    abc(idx-1)
    print(arr[idx],end=' ')
m = int(input())
abc(m)
