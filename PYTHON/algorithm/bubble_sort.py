lst = [8,3,12,10,1]
sorted = False
while sorted == False:
    sorted = True
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            lst[i], lst[i+1] = lst[i+1] , lst[i]
            sorted = False
print(*lst)