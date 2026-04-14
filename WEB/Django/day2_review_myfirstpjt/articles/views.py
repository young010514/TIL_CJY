from django.shortcuts import render

# Create your views here.
def index(request):

    info = {
        'name':'KEVIN',
        'age':21,
        'colors':['red','black','white'],

    }
    
    return render(request,'articles/index.html',info)
    