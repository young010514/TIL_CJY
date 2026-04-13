def main():
    u,i = KFC()
    print(f"대문자{u}개\n소문자{i}개")
def KFC():
    arr = list(input())
    u, i = 0, 0
    for x in arr:
        if x.isupper():u +=1
        else: i += 1

    return u, i
main()