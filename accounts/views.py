from django.shortcuts import redirect, render
from django.views.generic import CreateView
from .forms import CustomUserCreationForm, UserCreationForm

def SignupView(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else :
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html',{
        'form' : form
    })