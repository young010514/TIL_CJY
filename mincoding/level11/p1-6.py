arr = [3,4,1,3,2,7,3]
def main():
    num = int(input())
    result = False
    for x in arr:
        if x == num : result = True
    if result:
        print("발견")
    else:
        print("미발견")
main()