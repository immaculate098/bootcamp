from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import LoginForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            if password == "immaculate":  
                messages.success(request, 'Login successful!')
                return redirect('index_view')  
            else:
                messages.error(request, 'Invalid password!')
                return render(request, 'login.html', {'form': form, 'error_message': 'Invalid password!'})
        else:
            messages.error(request, 'Invalid form data. Please check your input.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
