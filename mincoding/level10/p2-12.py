def main():
    result = yesOrNo()
    print(result)
def yesOrNo():
    num = int(input())
    if num % 3 == 0 : return 7
    elif num % 3 == 1: return 35
    else : return 50
main()