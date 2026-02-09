import sys
sys.stdin = open("input_inout.txt", "r")

T = int(input())
for tc in range(1,T+1):
    lst = list(input())
    data = []
    result = 0
    bn = True
    for i in lst:
        if i == "(" or i == "{":
            data.append(i)
        elif i == ")":
            if data and data[-1] == "(":
                data.pop()
            else:
                bn = False
                break
        elif i == "}":
            if data and data[-1] == "{":
                data.pop()
            else:
                bn = False
                break
    if bn and data == []: result = 1
    print(f"#{tc} {result}")