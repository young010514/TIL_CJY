arr = ['D','F','G','D','A','Q']

def main():
    a, b = input().split()
    result = False
    for i in arr :
        if ord(a) <= ord (i) <= ord(b):
            result = True
            return result
        return result




main()