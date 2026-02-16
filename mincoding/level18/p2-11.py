lst=  list(input())
result = [0] * 5
st ="GHOST"
for i in lst:
    if i in st : result[st.index(i)] = 1
if sum(result) == 5 : print("존재")
else:print("존재하지 않음")