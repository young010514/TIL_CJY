a = input()
even, odd = a[::2], a[1::2]
if even.isalpha() and (even.isupper() or even.islower()) and odd.isalpha() and (odd.isupper() or odd.islower()):
    print("개구리문장")
else:print("일반문장")  
