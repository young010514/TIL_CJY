def findUpper(arr):
    cnt = 0
    for inner in arr:
        for data in inner:
            if data == data.upper() : cnt += 1
    print(f"대문자{cnt}개")
def findLower(arr):
    cnt = 0
    for inner in arr:
        for data in inner:
            if data == data.lower() : cnt += 1
    print(f"소문자{cnt}개")
    

def main():
    in_data = input().split()
    arr = []
    for i in range(2):
        arr.append([])
        for a in range(3):
            arr[i].append(in_data[a+3*i])
    findUpper(arr)
    findLower(arr)

main()