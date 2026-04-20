arr=[
    list('ABC'),
    list('AGH'),
    list('HIJ'),
    list('KAB'),
    list('ABC'),
]
result =[]
for inner in arr:
    result += inner
print(''.join(sorted(result)))