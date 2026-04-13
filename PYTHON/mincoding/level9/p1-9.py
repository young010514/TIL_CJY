arr = [['F','E','W'],['D','C','A']]
def main():
    n = input()
    return n

def findCh(c) :
    result = False
    for inner in arr:
        if c in inner : result = True
    if result : print("발견")
    else : print("미발견")

findCh(main())
