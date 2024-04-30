from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from.models import Student
from.forms import StudentForm
from django.shortcuts import redirect, get_object_or_404


def immy_view(request):
    students = Student.objects.all()
    return render(request, 'sitterlist.html', {'students':students})

def view_student(request,id):
    student =Student.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))

def add(request):
    if request.method =='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            new_sitter_name = form.cleaned_data['name']
            new_sitter_gender = form.cleaned_data['gender']
            new_sitter_location = form.cleaned_data['location']
            new_sitter_date_of_birth = form.cleaned_data ['date_of_birth']
            new_sitter_nin = form.cleaned_data['nin']
            new_sitter_religion = form.cleaned_data['religion']
            new_sitter_education = form.cleaned_data['education']
            new_sitter_contact = form.cleaned_data['contact']
            new_sitter_number = form.cleaned_data['sitter_number']
            new_sitter_next_of_kin = form.cleaned_data['next_of_kin']
            new_sitter_recommender_name = form.cleaned_data['recommender_name']
            new_sitter_recommender_contact = form.cleaned_data['recommender_contact']

            new_student = Student(
                name= new_sitter_name,
                gender= new_sitter_gender  ,
                location=  new_sitter_location ,
                date_of_birth= new_sitter_date_of_birth,
                nin=  new_sitter_nin,
                religion= new_sitter_religion ,
                education= new_sitter_education,
                contact=  new_sitter_contact,
                sitter_number=  new_sitter_number,
                next_of_kin= new_sitter_next_of_kin,
                recommender_name=new_sitter_recommender_name,
                recommender_contact= new_sitter_recommender_contact
            )
        new_student.save()
        return render(request, 'add.html',{
          'form': StudentForm(),  
          'success': True,
        })
    else:
       form=StudentForm()
    return render(request, 'add.html',{
      'form': StudentForm()  
      
    })


def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('immy_view') 


def edit_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('immy_view')
    else:
        form = StudentForm(instance=student)
        
    return render(request, 'edit.html', {'form': form})