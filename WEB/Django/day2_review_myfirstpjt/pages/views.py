from django.shortcuts import render

# Create your views here.
def index(request,name):
    message = request.GET.get('msg')
    context = {
        'message':message,
        'name':name,
    }
    return render(request, 'pages/index.html',context)