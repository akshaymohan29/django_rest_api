from django.shortcuts import render,redirect
from .models import Students
from .form import Students_form

def student_data(request):
    data=Students.objects.all()

    return render(request,'curdapp/stu.html', {'stud':data})

def student_form(request):
    form=Students_form()
    if request.method == "POST" :
        form=Students_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/students')
    return render(request ,'curdapp/stud-form.html',{'form':form})

def delete_student(request,id):
    student=Students.objects.get(id=id)
    student.delete()
    return redirect('/students')

def update_student(request,id):
    student=Students.objects.get(id=id)
    if request.method=='POST':
        form=Students_form(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('/students')

    return render(request ,'curdapp/update.html',{'student':student})