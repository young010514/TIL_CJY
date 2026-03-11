a = input()
b = input()
while 1:
    if b not in a:
        break
    idx = a.index(b)

    lst = a[:idx] + a[idx+len(b):]
    a = lst
if a : print(a)
else:print("Art!")