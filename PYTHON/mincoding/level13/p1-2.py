def main():
    age = int(input())
    a, b, c = moom(age)
    print(a,b,c)
def moom(num):
    return num-4, num+3, num *2
main()