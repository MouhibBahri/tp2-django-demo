from django.shortcuts import get_object_or_404, redirect, render

from .forms import TaskForm
from .models import Task


def task_list(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'form': form})


def task_toggle(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.done = not task.done
        task.save()
    return redirect('task_list')
