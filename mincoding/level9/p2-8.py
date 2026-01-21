def main():
    num = int(input())
    if num % 2 ==1:
        input2 = int(input())
        BBQ(input2)
    else :
        input2= input()
        KFC(input2)

def BBQ(num):
    for i in range(num):
        print(i + 1, end='')

def KFC(s):
    print(s*7)

main()