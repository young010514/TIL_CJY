lst = [3,7,4,1,2,6]
univer =[]
for i in range(2):
    univer.append(list(map(int,input().split())))
for inner in univer:
    for i in inner:
        if i in lst:
            print("OK", end=' ')
        else:
            print("NO", end=' ')
    print()
    