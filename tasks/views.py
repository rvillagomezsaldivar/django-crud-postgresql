from django.shortcuts import render, redirect
from .models import Tasks
from django.http import HttpResponse, JsonResponse

# Create your views here.
def list_tasks(request):
    tasks = Tasks.objects.all()
    return render(request,'list_tasks.html', {"tasks":tasks})

def create_task(request):
    #print(request.POST)
    task = Tasks(title=request.POST['title'], description=request.POST['description'])
    task.save()
    return redirect('/tasks/')

def listaTareas(request):
    list_tasks = list(Tasks.objects.values())
    return JsonResponse(list_tasks, safe=False)

def deleteTask(request, task_id):
    task = Tasks.objects.get(id=task_id)
    task.delete()
    return redirect('/tasks/')
