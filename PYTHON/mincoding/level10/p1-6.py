def main():
    a, b= map(int,input().split())
    if (a // b) % 2 ==0 : even(a // b)
    else :odd(a // b)
    printData(a+b)
def printData(value) :
    print(value)
def even(value):
    printData(value * 2)
def odd(value):
    printData(value - 10)
main()