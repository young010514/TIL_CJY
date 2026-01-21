arr = [['D','A','A'], ['B','C','D'], ['E','F','A'], ['A','A','D'], ['F','G','E']]
s = input()
result = []
for x, inner in enumerate(arr):
    for y, data in enumerate(inner):
        if data == s : 
            result.append((x,y))
[print(f"({x[0]},{x[1]})") for x in result]