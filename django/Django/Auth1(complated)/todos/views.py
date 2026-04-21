from django.shortcuts import render
from .models import Todo
from django.shortcuts import render, redirect 
from .forms import TodoForm
# Create your views here.


def index(request):
    works = Todo.objects.all()
    context = {
        'todo_list': works
    }
    return render(request, 'todos/index.html', context)



def create_todo(request):
    if request.method == 'POST':                      # POST 요청일 경우
        form = TodoForm(request.POST,request.FILES)   #유저가 작성한 내용을 form에 담은 후
        if form.is_valid():                           #작성된 내용이 유효한 정보라면 
            todo = form.save()                        #Database에 저장
            return redirect('todos:detail', todo.pk)
    else:                       #GET 요청일 경우
        form = TodoForm()       #유저가 작성할 form을 foms.py에 정의해 놓은 form을 가져온다
        
    context = {
        'form': form           # post요청 or get요청으로 완성된 form을
    }
    return render(request, 'todos/create_todo.html', context) # create.html문서로 보낸다


def detail(request, todo_pk):
    todo=Todo.objects.get(pk=todo_pk)
    context = {
        'todo': todo
    }
    return render(request, 'todos/detail.html', context)

def delete_todo(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('todos:index')
    else:
        return redirect('todos:detail', todo.pk)


    


def update_todo(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)                               # 수정 전 기록이 담긴 객체 (todo)
    if request.method == 'POST':
        form = TodoForm(request.POST, request.FILES, instance=todo)    # 새로운 기록이 담긴 객체 (form)
        if form.is_valid():
            todo = form.save()                                       # todo객체에 새로운기록을 넣고 DB에 저장
            return redirect('todos:detail', todo.pk)
    else:
        form = TodoForm(instance=todo)                  # get요청일 경우 수정전 기록이 담긴 객체 (todo)
    context = {
        'todo': todo,                                    
        'form': form                                    # (post라면) form에는 유효하지 않은정보 또는 
    }                                                   # (get이라면) 빈 modelform이 전달 될 것임
    return render(request, 'todos/update_todo.html', context)


