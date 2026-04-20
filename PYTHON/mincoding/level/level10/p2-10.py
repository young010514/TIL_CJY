arr = [
    [1, None,None,None,None,],
    [1, None,1,None,None,],
    [1, 1,None,1,None,],
    [1, None,1,None,None,],
    [None,1, None,None,1],
    [None,None,None,1, None,],
    [1, 1,None,None,None,],
]
def main():
    num = input1()
    cnt = process(num, arr)
    output(cnt)

def input1():
    num = int(input())
    return num

def process(num, arr):
    cnt =0
    for x in arr:
        if x[num] ==1 : cnt +=1
    return cnt
def output(cnt):
    print(cnt)




main()
