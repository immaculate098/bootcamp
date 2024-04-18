from django.shortcuts import render, redirect
from .forms import ResetPasswordForm

def resetpassword_view(request):
    if request.method == 'POST':
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            if password == confirm_password:
                
                return redirect('newpassword_view')  
            else:
                
                error_message = 'Passwords do not match!'
                return render(request, 'resetpassword.html', {'form': form, 'error_message': error_message})
        else:
            
            return render(request, 'resetpassword.html', {'form': form})
    else:
        
        form = ResetPasswordForm()
        return render(request, 'resetpassword.html', {'form': form})
