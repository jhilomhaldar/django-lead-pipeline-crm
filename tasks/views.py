from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Task
from .forms import TaskForm
from django.views.decorators.http import require_POST



def task_list(request):
    tasks = Task.objects.select_related('lead', 'deal', 'assigned_to').order_by('due_date', 'due_time')

    q = request.GET.get('q', '')
    status = request.GET.get('status', '')
    priority = request.GET.get('priority', '')
    assigned_to = request.GET.get('assigned_to', '')

    if q:
        tasks = tasks.filter(title__icontains=q)

    if status:
        tasks = tasks.filter(status=status)

    if priority:
        tasks = tasks.filter(priority=priority)

    if assigned_to:
        tasks = tasks.filter(assigned_to_id=assigned_to)

    today = timezone.localdate()

    total_tasks = tasks.count()
    overdue_tasks = tasks.filter(due_date__lt=today).exclude(status__in=['completed', 'cancelled']).count()
    due_today_tasks = tasks.filter(due_date=today).exclude(status__in=['completed', 'cancelled']).count()
    completed_tasks = tasks.filter(status='completed').count()

    return render(request, 'tasks/task_list.html', {
        'tasks': tasks,
        'today': today,
        'users': User.objects.all(),
        'total_tasks': total_tasks,
        'overdue_tasks': overdue_tasks,
        'due_today_tasks': due_today_tasks,
        'completed_tasks': completed_tasks,
    })


def task_add(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task created successfully.')
            return redirect('task_list')
    else:
        initial_data = {}

        lead_id = request.GET.get('lead')
        deal_id = request.GET.get('deal')

        if lead_id:
            initial_data['lead'] = lead_id

        if deal_id:
            initial_data['deal'] = deal_id

        form = TaskForm(initial=initial_data)

    return render(request, 'tasks/task_form.html', {
        'form': form,
        'page_title': 'Add Task'
    })


def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated successfully.')
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)

    return render(request, 'tasks/task_form.html', {
        'form': form,
        'page_title': 'Edit Task'
    })


def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Task deleted successfully.')
        return redirect('task_list')

    return render(request, 'tasks/task_confirm_delete.html', {'task': task})


@require_POST
def task_quick_complete(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if task.status != 'completed':
        task.status = 'completed'
        task.save()
        messages.success(request, f'Task "{task.title}" marked as completed.')

    return redirect('task_list')