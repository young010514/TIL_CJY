import sys
sys.stdin =open("input_calcul.txt","r")

from collections import deque
for tc in range(1,11):
    n = int(input())

    left = [0] * (n+1)
    right = [0] * (n+1)
    par = [0] * (n+1)
    data =[0] * (n+1)


    for i in range(n):
        lst = input().split()
        idx = int(lst[0])
        data[idx] = lst[1]
        if len(lst) == 4:
            left[idx] = int(lst[2])
            right[idx] = int(lst[3])
            par[int(lst[2])] = idx
            par[int(lst[3])] = idx
    result = deque()
    def post_order(T):
        global result
        if T:
            post_order(left[T])
            post_order(right[T])
            result.append(data[T])
            if data[T].isdigit() : result.append(int(data[T]))
            else:
                i1 = result.popleft()
                i2 = result.popleft()
                if data[T] == "*" : result.append(i1*i2)
                elif data[T] == "-" : result.append(i1-i2)
                elif data[T] == "/" : result.append(i1/i2)
                elif data[T] == "+" : result.append(i1+i2)
                print(result[-1])
    post_order(1+par[1:].index(0))
    # print(*result)
    # print(int(result[0]))
