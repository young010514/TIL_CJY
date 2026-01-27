arr1 = [['D','A','D'],['Q','W','Q'],['A','S','D'],['A','S','D']]
def main():
    n = input()
    find(n)
    pass

def find(s):
    result = False
    for inner in arr1:
        if s in inner: result = True
    if result : print("존재")
    else:print("없음")
main()