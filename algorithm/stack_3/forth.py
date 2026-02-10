import sys
sys.stdin =open("input_forth.txt","r")

T = int(input())
for tc in range(1,T+1):
    lst = input().split()
    num_lst = []
    for i in lst:
        if i.isdigit():
            num_lst.append(int(i))
        else:
            if i == ".":
                if len(num_lst) == 1:
                    result = num_lst[0]
                else:
                    result = "error"
            elif len(num_lst) < 2:
                result = "error"
                break
            else:
                x= num_lst.pop()
                y = num_lst.pop()
                if i == "+" :
                    num_lst.append(x+y)
                elif i == "*" :
                    num_lst.append(x*y)
                elif i == "/":
                    num_lst.append(y//x)
                elif i == "-":
                    num_lst.append(y-x)


    print(f"#{tc} {result}")