def main():
    n_list = input1()
    
    calc(*n_list)

def input1():
    return map(int,input().split())
def calc(*numbers):
    print(sum(numbers))

main()