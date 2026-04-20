result = [0]*200
lst = list(input())
for i in lst: result[ord(i)] += 1
for x in range(200):
    if result[x] != 0:print(f"{chr(x)}:{result[x]}")