def abc(level):
    if level == 2:
        print("2",end='')
        return
    print("2",end='')
    for i in range(2):
        abc(level+1)
        print("2",end='')


abc(0)

print("****")
print(len(list("2222222222222")))