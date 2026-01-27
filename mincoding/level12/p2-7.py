arr, len_arr = [], []
for i in range(3):
    n = input()
    arr.append(n)
    len_arr.append(len(n))
print(arr[len_arr.index(max(len_arr))])