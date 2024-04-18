from django.shortcuts import render, redirect
from .forms import SitterRegistrationForm

def sitterform_view(request):
    if request.method == 'POST':
        form = SitterRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index_view')  # Redirect to a success page
    else:
        form = SitterRegistrationForm()
    return render(request, 'sitterform.html', {'form': form})
