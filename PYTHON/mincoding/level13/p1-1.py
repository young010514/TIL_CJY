def main():
    a, b = getName()
    if ord(a) > ord(b) : print(b)
    else:print(a)

def getName():
    a, b =input().split()
    return a, b

main()