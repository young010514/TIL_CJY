lst = [
    ['BHC', 'BBQ', 'KFC'],
    ['MC', '7AVE', 'PAPA'],
    ['DHC', 'OBS', 'MOMS'],
]
direcitons = [
    (-1, 0),
    (0, -1),
    (1, 0),
    (0, 1),
]
a,b=map(int,input().split())

st = ''
for i,j in direcitons:
    if 0<=a + i < 3 and 0<= b+j <3:
        st += lst[a+i][b+j]
print(st)