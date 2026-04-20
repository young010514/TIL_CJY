a = input()
n = int(input())
arr= [input() for _ in range(n)]
for i in arr:
    if a in i : print("O")
    else:print("X")