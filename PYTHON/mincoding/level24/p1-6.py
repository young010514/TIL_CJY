st = input().lower()
c1 = st.count("pass")
c2 = st.count("fail")

print(f"{100*c1//(c1+c2)}%")