arr = [['D','A','C','C','D'],['S','D','F','A','E'],['E','E','T','J','H']]
def main():
    input1()
def input1():
    n = input()
    s = check(n)
    if s == 1 :print("있음")
    elif s == 0: print("없음")
def check(value):
    for inner in arr:
        if value in inner: return 1
        else :return 0
main()