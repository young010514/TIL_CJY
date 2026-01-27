arr = [[1,1,1],[1,2,1],[3,6,3]]
def main():
    num = int(input())
    print(Count(num))

def Count(num):
    cnt =0
    for inner in arr:
        for x in inner:
            if x == num : cnt+= 1
    return cnt

main()