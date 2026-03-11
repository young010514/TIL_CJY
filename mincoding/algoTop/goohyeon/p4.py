h = int(input())
m = input()
hours = ["","one","two",'three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','quater','sixteen','seventeen','eighteen','nineteen','twenty','twenty one','twenty two','twenty three','twenty four','twenty five','twenty six','twenty seven','twenty eight','twenty nine']

def clock(h,m):
    if m == "00" : return f"{hours[h]} o' clock"
    m = int(m)
    if m == 1 : return f"one minute past {hours[h]}"
    if m == 59 : return f"one minute to {hours[h+1] }"
    if m == 30 :
        return f"half past {hours[h]}"
    if m == 15:
        return f"quarter past {hours[h]}"
    if m == 45 and h < 12 :
        return f"quarter to {hours[h+1]}"
    if m == 45 and h == 12:
        return f"quarter to one"
    if m < 30:
        return f"{hours[m]} minutes past {hours[h]}"
    if m > 30  and h < 12: return f"{hours[60-m]} minutes to {hours[h+1]}"
    if m > 30 and h == 12 : return f"{hours[60-m]} minutes to one"
result = clock(h,m)
print(result)