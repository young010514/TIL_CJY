project = {
    "upper0" : {
        'num':5, 
        'id':"G", 
        'vect':[1,2,3,4], 
    },
    "upper10" : {
        'num':8, 
        'id':"T", 
        'vect':[5,1,2,3], 
    },
    "upper100" : {
        'num':10, 
        'id':"Q", 
        'vect':[9,1,6,2], 
    },
}
n = int(input())
if n <10 :
    z = project['upper0']
elif n <100 :
    z = project['upper10']
else:
    z = project['upper100']

print(z['num'])
print(z['id'])
[print(x, end = ' ') for x in z['vect']]