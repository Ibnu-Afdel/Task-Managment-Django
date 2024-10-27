from django.shortcuts import redirect, render , get_object_or_404 , reverse

from .models import Task , Category 
from .forms import TaskForm , CommentForm
from django.contrib.auth.decorators import login_required
from personal_task.models import MyTaskModel


def home(request):
    categories = Category.objects.all()
    tasks = Task.objects.all()
    personal_tasks = MyTaskModel.objects.all()[:3]

    selected_category = request.GET.get('category')
    if selected_category:
        tasks = tasks.filter(category__id=selected_category)
    

    tasks = tasks[:3] 
    context = {'tasks': tasks, 'categories': categories , 'personal_tasks':personal_tasks}
    return render(request, 'social/home.html', context)


@login_required
def detail(request, pk):
    task_detail = get_object_or_404(Task, pk=pk)
    # edit_url = reverse('edit_task', kwargs={'pk': task_detail.pk})
    # delete_url = reverse('delete_task', kwargs={'pk': task_detail.pk})
    
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.task = task_detail
            comment.commenter = request.user
            comment.save()
            return redirect('detail', pk=pk)
    else:
        comment_form = CommentForm()

    context = {'task_detail': task_detail, 'comment_form': comment_form, }
    return render(request, 'social/detail.html', context)

@login_required()
def create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            user = request.user
            form.instance.posted_by = user
            form.save()
            return redirect('home')
    else :
        form = TaskForm()
    return render(request, 'social/create.html',{
        'form':form
    })

@login_required()
def update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task )
        if form.is_valid():
            form.save()
            return redirect('home')
    else :
        form = TaskForm(instance=task)
    return render(request, 'social/create.html',{
        'form':form
    })

@login_required()
def delete(request,pk):
    task = Task.objects.get(pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('home')
    context = {'task' : task}
    return render(request, 'social/delete.html', context)


@login_required()
def all_post(request):
    categories = Category.objects.all()
    tasks = Task.objects.all()
    all_tasks = Task.objects.all()

    selected_category = request.GET.get('category')
    if selected_category:
        tasks = tasks.filter(category__id=selected_category)

    context = {'tasks': tasks, 'categories': categories , 'all_tasks' : all_tasks}
    return render(request, 'social/all_post.html', context)


   