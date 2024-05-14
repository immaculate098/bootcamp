from django.shortcuts import render, redirect
from .models import Sitter
from .forms import SitterForm
from django.views import View



def sitter_management(request):
    if request.method == 'POST':
        filter_value = request.POST.get('filter')
        if filter_value:
            if filter_value == 'on_duty':
                sitters = Sitter.objects.filter(on_duty=True)
            elif filter_value == 'off_duty':
                sitters = Sitter.objects.filter(on_duty=False)
        else:
            sitters = Sitter.objects.all()
    else:
        filter_value = request.GET.get('filter')
        if filter_value:
            if filter_value == 'on_duty':
                sitters = Sitter.objects.filter(on_duty=True)
            elif filter_value == 'off_duty':
                sitters = Sitter.objects.filter(on_duty=False)
        else:
            sitters = Sitter.objects.all()

    return render(request, 'sitterduty.html', {'sitters': sitters})



def add_sitter(request):
    if request.method == 'POST':
        form = SitterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sitter_management')
    else:
        form = SitterForm()
    return render(request, 'add_sitter.html', {'form': form})




def save_changes(request):
    if request.method == 'POST': 
        selected_sitter_ids = request.POST.getlist('selected_sitters')
        for sitter_id in selected_sitter_ids:
            try:
                sitter = Sitter.objects.get(id=sitter_id)
                sitter.on_duty = not sitter.on_duty  
                sitter.save() 
            except Sitter.DoesNotExist:
                pass
        return redirect('sitter_management')
    else:
        return redirect('sitter_management')


class DeleteSitterView(View):
    def post(self, request, sitter_id):
        sitter = Sitter.objects.get(id=sitter_id)
        sitter.delete()
        return redirect('sitter_management')


class UpdateSitterView(View):
    def get(self, request, sitter_id):
        sitter = Sitter.objects.get(id=sitter_id)
        form = SitterForm(instance=sitter)
        return render(request, 'update.html', {'form': form})

    def post(self, request, sitter_id):
        sitter = Sitter.objects.get(id=sitter_id)
        form = SitterForm(request.POST, instance=sitter)
        if form.is_valid():
            form.save()
            return redirect('sitter_management')
        else:
            return render(request, 'update.html', {'form': form})