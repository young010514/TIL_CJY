n = int(input())
y,x=  5,5
for _ in range(n):
    s = input().strip()
    if s == "up":
        y -= 1
    elif s == "down" :
        y += 1
    elif s == "left":
        x -= 1
    elif s == "right":
        x += 1
    elif s == "click":
        print(f"{y},{x}")