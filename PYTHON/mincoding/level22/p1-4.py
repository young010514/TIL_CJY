arr = [input().strip() for _ in range(5)]
result = arr.count("up") - arr.count("down")
if result >= 0:
    print(f"{result +1}")
else:
    print(f"B{abs(result)}")