arr = list('ABCZETQ')
inputarr = list(input())
for i in inputarr:
    if i in arr:
        print(f"{i}=마을사람")
    else:print(f"{i}=외부사람")