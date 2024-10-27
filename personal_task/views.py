from django.shortcuts import redirect, render , get_object_or_404
from .models import MyTaskModel
from django.db.models import Q 
from django.db.models import Count
from .forms import MyTaskForm
from django.contrib.auth.decorators import login_required


@login_required()
def dashboard(request):
    tasks = MyTaskModel.objects.all()  # Fetch all tasks initially
    selected_filter = request.GET.get('filter', '')  # Get filter value from query string (optional)
    selected_order = request.GET.get('order', '')  # Get order value from query string (optional)

    if selected_filter == 'latest':
        tasks = tasks.order_by('-created_in')  # Order by latest first
    elif selected_filter == 'oldest':
        tasks = tasks.order_by('created_in')  # Order by oldest first

    if selected_order:
        # Implement custom ordering based on selected_order (optional)
        pass

    total_tasks = tasks.count()
    priority_counts = MyTaskModel.objects.aggregate(
    high_tasks=Count('id', filter=Q(priority='high')),
    medium_tasks=Count('id', filter=Q(priority='medium')),
    low_tasks=Count('id', filter=Q(priority='low')),
)
    context = {
        'tasks': tasks,
        'selected_filter': selected_filter,
        'selected_order': selected_order,
        'total_tasks': total_tasks,
        'priority_counts': priority_counts,
    }

    return render(request, 'task/dashboard.html', context)
@login_required()
def create_task(request):
    if request.method == 'POST':
        form = MyTaskForm(request.POST)
        if form.is_valid():
            user = request.user
            form.instance.owner = user
            form.save()
            return redirect('dashboard')
    else :
        form =  MyTaskForm()
    context = {'form' : form}
    return render(request, 'task/create_task.html', context)

@login_required()
def update_task(request, pk):
    model = get_object_or_404(MyTaskModel, pk=pk)
    if request.method == 'POST':
        form = MyTaskForm(request.POST, instance=model)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else :
        form = MyTaskForm(instance=model)
    context = {'form' : form}
    return render(request, 'task/create_task.html', context)

@login_required()
def delete_task(request,pk):
    model = MyTaskModel.objects.get(pk=pk)
    if request.method == 'POST':
        model.delete()
        return redirect('dashboard')
    context = {'model' : model}
    return render(request, 'task/delete_task.html',context)

@login_required()
def detail_task(request,pk):
    model = MyTaskModel.objects.get(pk=pk)

    all_tasks = MyTaskModel.objects.all().count()    
    task_number = all_tasks - MyTaskModel.objects.filter(pk__lt=pk).count()
    context = {'model' : model , 'task_number': task_number, }
    return render(request, 'task/detail_task.html', context)

