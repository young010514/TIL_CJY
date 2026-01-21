result = []
for a in range(3):
    result.append([])
    for b in range(3):
        result[a].append(chr(ord("A")+b+3*a))

n1, n2= map(int, input().split())
n3, n4= map(int, input().split())
result[n1][n2], result[n3][n4] = result[n3][n4], result[n1][n2]

for inner in result:
    print("".join(inner))