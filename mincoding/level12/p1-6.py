arr = list("MINQUEST")  
def main():
    s1 = input()
    s2 = input()
    s3 = input()
    l1 = Length(s1)
    l2 = Length(s2)
    l3 = Length(s3)
    print(f'{s1}={l1}')
    print(f'{s2}={l2}')
    print(f'{s3}={l3}')
def Length(s):
    return arr.index(s)
    


main()