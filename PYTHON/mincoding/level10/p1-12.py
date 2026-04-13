def main():
    num = int(input())
    CountDown(num)

def CountDown(value):
    if value<1 :
        return
    print(value, end=' ')
    CountDown(value - 1)



main()