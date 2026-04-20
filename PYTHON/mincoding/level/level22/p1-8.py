lst=[[[2,4],[1,5]],
[[2,3],[3,6]],
[[7,3],[1,5]]]
n = int(input())
max_data = max(lst[n][0] + lst[n][1])
min_data = min(lst[n][0] + lst[n][1])

print(f"MAX={max_data}")
print(f"MIN={min_data}")