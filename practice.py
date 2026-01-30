N,A,B,C,D=map(int,input().split())
shelters=[tuple(map(int,input().split())) for _ in range(N)]
 
# Please write your code here.
rag = []
for i in range(C,D +1):
    rag.append((A * i, B * i))
result = []
for x,y in shelters:
    for a,b in rag:
        result.append(abs(x-a) + abs(y-b))
print(min(result))
