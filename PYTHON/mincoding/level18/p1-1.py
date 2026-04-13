arr = [
    [65000,35,42,70],
    [70,35,65000,1300],
    [65000,30000,38,42],
]
result = {}
for inner in arr:
    for x in inner:
        if result.get(x):
            result[x] += 1
        else:
            result[x] = 1
val = sorted(result.values())[-1]

for k,v in result.items():
    if v== val :
        print(k)
