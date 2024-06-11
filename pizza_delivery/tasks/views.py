from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Task, KitchenTask
from .forms import TaskForm
import json

def home(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            department = form.cleaned_data['department']
            form.save()
            return redirect(f'/{department}')
    else:
        form = TaskForm()
    return render(request, 'home.html', {'form': form})

def save_task(request):
    if request.method == 'POST':
        location = request.POST.get('location')
        department = request.POST.get('department')
        shift = request.POST.get('shift')
        name = request.POST.get('name')
        date = request.POST.get('date')

        task = Task.objects.create(
            location=location,
            department=department,
            shift=shift,
            name=name,
            date=date
        )
        task.save()

        if department == 'kitchen':
            return redirect('kitchen')
        elif department == 'terminal':
            return redirect('terminal')
        elif department == 'driver':
            return redirect('driver')

    return render(request, 'home.html')

def kitchen(request):
    if request.method == 'POST' and request.is_ajax():
        data = json.loads(request.body)
        date = data.get('date')
        task_status = data.get('task_status', [])

        if not date:
            return JsonResponse({'error': 'Date is required'}, status=400)

        task = Task.objects.filter(date=date, department='kitchen').first()

        if not task:
            return JsonResponse({'error': 'Task not found'}, status=404)

        kitchen_task, created = KitchenTask.objects.get_or_create(task=task)
        kitchen_task.make_juice_completed = 'make_juice' in task_status
        kitchen_task.make_pizza_completed = 'make_pizza' in task_status
        kitchen_task.save()

        return JsonResponse({'success': True})

    return render(request, 'kitchen.html')

def terminal(request):
    if request.method == 'POST' and request.is_ajax():
        data = json.loads(request.body)
        date = data.get('date')
        task_status = data.get('task_status', [])

        if not date:
            return JsonResponse({'error': 'Date is required'}, status=400)

        task = Task.objects.filter(date=date, department='terminal').first()

        if not task:
            return JsonResponse({'error': 'Task not found'}, status=404)

        # kitchen_task, created = KitchenTask.objects.get_or_create(task=task)
        # kitchen_task.make_juice_completed = 'make_juice' in task_status
        # kitchen_task.make_pizza_completed = 'make_pizza' in task_status
        # kitchen_task.save()
        #
        # return JsonResponse({'success': True})

    return render(request, 'terminal.html')
def driver(request):
    return render(request, 'driver.html')

def dashboard(request):
    tasks_with_completion_status = []
    tasks = Task.objects.all()
    for task in tasks:
        kitchen_task = KitchenTask.objects.filter(task=task).first()
        all_completed = (
            kitchen_task and
            kitchen_task.make_juice_completed and
            kitchen_task.make_pizza_completed
        )
        tasks_with_completion_status.append({
            'date': task.date,
            'location': task.location,
            'department': task.department,
            'shift': task.shift,
            'name': task.name,
            'make_juice_completed': kitchen_task.make_juice_completed if kitchen_task else False,
            'make_pizza_completed': kitchen_task.make_pizza_completed if kitchen_task else False,
            'all_completed': 'Yes' if (
                        kitchen_task and kitchen_task.make_juice_completed and kitchen_task.make_pizza_completed) else (
                'No' if kitchen_task else 'N/A')
        })

    return render(request, 'dashboard.html', {'tasks_with_completion_status': tasks_with_completion_status})
