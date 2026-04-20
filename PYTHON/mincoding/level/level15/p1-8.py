inputarr= []
lenarr= []
for i in range(5):
    a = input()
    inputarr.append(a)
    lenarr.append(len(a))
print(inputarr[lenarr.index(max(lenarr))])