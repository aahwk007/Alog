from django.shortcuts import render, redirect
from .models import Todo
from .forms import T_form
# Create your views here.


def home(request):
    todos = Todo.objects.all()
    return render(request, 'home.html', {'todos': todos})


def todo(request, pk):
    todo = Todo.objects.get(id=pk)

    return render(request, 'room.html', {'todo': todo})


def create_todo(request):
    form = T_form()
    if request.method == 'POST':
        form = T_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'c.html', {'form': form})


def update_todo(request, pk):
    todo = Todo.objects.get(id=pk)
    form = T_form(instance=todo)

    if request.method == 'POST':
        form = T_form(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'c.html', {'form': form})


def delete_todo(request, pk):
    todo = Todo.objects.get(id=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('home')
    return render(request, 'd.html', {'todo': todo})
