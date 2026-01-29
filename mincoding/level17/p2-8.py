map1 = [[3,55,42],[-5,-9,-10]]
pix = [
    list(map(int,input().split())),
    list(map(int,input().split())),
]
result =[['N','N'],['N','N']]
for inner in pix:
    for x in inner:
        for inn in map1:
            if x in inn:
                result[pix.index(inner)][inner.index(x)] = 'Y'
for i in result:
    print(' '.join(i))
