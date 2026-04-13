def main():
    arr = [input(), input(),input()]
    CountLine(arr)
def CountLine(arr):
    for i in arr:
        print(f"{len(i)}={i}")
main()