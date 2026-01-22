n = int(input())
if n % 5 == 1:
    arr = [[9,6,3],[8,5,2],[7,4,1]]
elif n% 5 == 2:
    arr = [[7,8,9],[4,5,6],[1,2,3]]
else:
    arr = [[10,13,16],[11,14,17],[12,15,18]]
for inner in arr :
    [print(x, end=' ') for x in inner]
    print()