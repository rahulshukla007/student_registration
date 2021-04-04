from django.shortcuts import render, redirect
from . forms import Studentform
from . models import Student
# Create your views here.

#this function is used for displaying & inserting the data
def home(request):
    if request.method == 'POST':
        fm = Studentform(request.POST)
        print('fm', fm)
        if fm.is_valid():
            fm.save()
    fm = Studentform()
    stud = Student.objects.all()
    return render(request, 'index.html', {'fm':fm, 'stud':stud})


#this code is for updation
def edit(request, id):
    if request.method == 'POST':
        data = Student.objects.get(pk=id)
        fm = Studentform(request.POST, instance=data)
        if fm.is_valid():
            fm.save()
        return redirect('home')

    data = Student.objects.get(pk=id)
    fm = Studentform(instance=data)
    return render(request, 'update.html', {'fm':fm})

# this code is for deletion
def delete(request, id):
    data = Student.objects.get(pk=id)
    data.delete()
    return redirect('home')


