from django.shortcuts import render
from django.http import HttpResponse
from .forms import VerificationForm

def verifypassword_view(request):
    if request.method == 'POST':
        code = request.POST.get('code', '')
        if len(code) > 6:
            error_message = 'Invalid digit number!'
            return render(request, 'verifypassword.html', {'error_message': error_message})
        
        
        code = request.POST.get('code', '')
        if len(code) < 6:
            error_message = 'Invalid digit number!'
            return render(request, 'verifypassword.html', {'error_message': error_message})
        


        else:
    
                  return render(request, 'resetpassword.html', {'success_message': 'Verification successful!'})
    else:
        return render(request, 'verifypassword.html')




 