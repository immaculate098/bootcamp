
from django.shortcuts import render, redirect
from .forms import ForgotPasswordForm

def forgot_view(request):
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
           
            return redirect('verifypassword_view') 
    else:
        form = ForgotPasswordForm()
    return render(request, 'forgot.html', {'form': form})

