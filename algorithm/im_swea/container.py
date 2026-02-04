import sys
sys.stdin = open("input_container.txt","r")

T = int(input())
for t in range(T):
    N,M = map(int,input().split())
    lst1 = list(map(int,input().split()))
    lst2 = list(map(int, input().split()))

    # 내림차순으로 정렬
    lst1.sort(reverse=True)
    lst2.sort(reverse=True)

    result = 0
    while lst1 and lst2 :
        if lst1[0] > lst2[0] :
            lst1.pop(0)
        else:
            result += lst1.pop(0)
            lst2.pop(0)

    print(f"#{t+1} {result}")
