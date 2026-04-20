arr = ['D','F','G','D','A','Q']

def main():
    a, b = input().split()
    result = False
    for i in arr :
        if ord(a) <= ord(i) <= ord(b):
            result = True
            return result
    return result

result = main()
if result : print("발견!!!")
else:print("미발견!!!")