town = [
    list('CDA'),
    list('BMZ'),
    list('QPO'),
]
black = list(input())
cnt =0
for inner in town:
    for x in inner:
        if x in black : cnt+= 1
print(f'{cnt}명')