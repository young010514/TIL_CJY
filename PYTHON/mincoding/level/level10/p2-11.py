def main():
    num = int(input())
    run(num)
def run(num):
    if num < 10 :
        arr = [[1,2,3],[4,5,6],[7,8,9]]
    elif num >= 10:
        arr = [[3,2,1],[6,5,4],[9,8,7]]

    for inner in arr:
        [print(x, end='') for x in inner]
        print()



main()