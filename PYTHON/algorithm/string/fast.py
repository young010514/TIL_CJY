
result = "bana" in "banana"

print(result)

result = "banana".count("nab")

print(result)

T = int(input())
for t in range(T):
    st1,st2 = input().split()
    cnt = st1.count(st2)
    print(f"#{t+1} {len(st1) - len(st2) * cnt + cnt}")