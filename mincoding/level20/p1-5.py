def main():
    st = input()
    abc(st, 0)
def abc(st, idx):
    if idx == len(st):
        print()
        return

    print(st[idx], end='')
    abc(st,idx+1)
    print(st[idx],end='')

main()
