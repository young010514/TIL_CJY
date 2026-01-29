arr = [
    [1,3,3,5,1],
    [3,6,2,4,2],
    [1,9,2,6,5],
]
from collections import defaultdict
arr_to_dict = defaultdict(int)
for inner in arr:
    for x in inner:
        arr_to_dict[x] += 1

num = int(input())
result = []
for k,v in dict(arr_to_dict).items():
    if v == num :
        result.append(k)
[print(x,end=' ') for x in sorted(result)]