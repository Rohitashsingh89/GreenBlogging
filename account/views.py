from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import EmailAuthenticationForm, UserRegistrationForm
from django.shortcuts import render, redirect
from .models import UserProfile

def user_register(request):
    form = UserRegistrationForm()

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)

            user = form.cleaned_data.get('username')
            messages.success(request, "Account was created for " + user)
            return redirect('home') 
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f" {error}")        

    context = {'form': form}
    return render(request, 'register.html', context)


# Authentication
def user_login(request):
    if request.method == 'POST':
        form = EmailAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.cleaned_data.get('username')
            login(request, form.get_user())
            return redirect('home')
        else:
            messages.info(request, 'username or password are incorrect!!')
    else:
        form = EmailAuthenticationForm()
    
    return render(request, 'login.html', {'form': form})
