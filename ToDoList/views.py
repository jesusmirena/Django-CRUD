from multiprocessing import context
from django.shortcuts import redirect, render
from .models import Task
from .forms import taskForm


def home(request):
    tasks = Task.objects.all()
    context = {"tasks": tasks}
    return render(request, "ToDoList/home.html", context)


def add(request):
    form = taskForm(request.POST)
    if request.method == "POST":
        if form.is_valid:
            form.save()
            return redirect("home")
    else:
        taskForm()
    context = {"form": form}
    return render(request, "ToDoList/add.html", context)


def delete(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect("home")


def edit(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == "POST":
        form = taskForm(request.POST, instance=task)
        if form.is_valid:
            form.save()
            return redirect("home")
    else:
        form = taskForm(instance=task)
    context = {"form": form}
    return render(request, "ToDoList/edit.html", context)
