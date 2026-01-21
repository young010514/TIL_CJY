person = {}
arr = list(map(int,input().split()))
person['a'] = {
    'age':arr[0],
    'height': arr[1],
}
person['b'] = {
    'age':arr[2],
    'height': arr[3],
}
age_list = [person[x]['age'] for x in person]
height_list = [person[x]['height'] for x in person]

print(sum(age_list)//len(age_list), sum(height_list)//len(height_list))