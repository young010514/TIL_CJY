bit = list(map(int,input().split()))
vect = [3,5,4,2,6,6,5]

for i in range(len(bit)):
    if not bit[i]:
        vect[i] = 0
for i in range(len(vect)):
    if vect[i] :
        vect[i] = 7
[print(x,end='') for x in vect]
