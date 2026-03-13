import sys
sys.stdin = open("input_stone.txt","r")

def drop(arr):
    arr2 = list(map(list,zip(*arr[::-1])))
    for i in range(len(arr2)):

        for j in range(len(arr2[0])):

            return

def bomb(arr):
    return


T = int(input())
for tc in range(1,T+1):
    n,w,h = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(h)]

    arr2 = list(map(list,zip(*arr[::-1])))
    print(arr2)



