arr = [[3,2,6,2,4],[1,4,2,6,5]]
def main():
    target = int(input())
    result = KFC(target)
    if result:
        print("값이 존재합니다")
    else:print("값이 없습니다")
def KFC(target):
    result = 0
    for inner in arr:
        if target in inner:
            result =1
    return result

main()