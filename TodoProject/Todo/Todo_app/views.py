from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Task
from .form import TaskForm

# Create your views here.
def home(request):
    context = {'success': False}

    if request.method == "POST":
        title = request.POST['title']
        desc = request.POST['desc']
        print(title, desc)
        ins = Task(taskTitle=title, taskDesc=desc)
        ins.save()
        context = {'success':True}
    return render(request,"home.html",context)

def task(request):
    allTasks = Task.objects.all()
    context = {"tasks": allTasks}
    return render(request,"task.html", context)

def update(request,pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('task')
    context = {'form':form}
    return render(request, 'update.html',context)

def delete(request,pk):
    item = Task.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('task')
    context = {'item':item}
    return render(request, 'delete.html')