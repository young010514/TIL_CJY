arr = [['a','b','E'],['E',2,'W'],[3,2,4]]
for inner in arr:
    for x in inner:
        if type(x) == int :print(x+5, end=' ')
        elif x.isupper():print(x.lower(), end=' ')
        else:print(x.upper(),end=' ')
    print()