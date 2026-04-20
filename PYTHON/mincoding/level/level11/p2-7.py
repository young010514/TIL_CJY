arr = [['a','b','d'],['e','w','z'],['q','v','a']]
def input1():
    a = input()
    return a
def process(a):
    result = False
    for inner in arr:
        if a.lower() in inner:
            result = True
    if result: print("존재")
    else:print("없음")
process(input1())