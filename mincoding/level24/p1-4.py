n = list(input())
lst = list("ABCDEFGHIJK")
result = [0] * len(lst)
for idx,i in enumerate(lst):
    result[idx] = n.count(i)

print(lst[result.index(max(result))])
print(lst[result.index(min(result))])
