from django.shortcuts import render, redirect
from . forms import Studentform, CreateUserForm
from . models import Student
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url = 'login')
#this function is used for displaying & inserting the data
def home(request):
    if request.method == 'POST':
        fm = Studentform(request.POST)
        print('fm', fm)
        if fm.is_valid():
            fm.save()
    fm = Studentform()
    stud = Student.objects.all()
    #using pagination thing
    paginator = Paginator(stud,3)
    print('paginator', paginator)
    page_number = request.GET.get('page')
    print('page_number', page_number)
    page_obj = paginator.get_page(page_number)
    print('page_obj', page_obj)

    return render(request, 'index.html', {'fm':fm, 'page_obj':page_obj})

@login_required(login_url = 'login')
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

@login_required(login_url = 'login')
# this code is for deletion
def delete(request, id):
    data = Student.objects.get(pk=id)
    data.delete()
    return redirect('home')


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            fm = CreateUserForm(request.POST)
            print("fm", fm)
            if fm.is_valid():
                fm.save()
                user = fm.cleaned_data.get('username')
                messages.success(request, f'account was creater for {user}')
                return redirect('login')
    form = CreateUserForm()
    context = {'form':form}
    return render(request, 'signup.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            print(request.POST)
            username = request.POST.get('username')
            print('username', username)
            password = request.POST.get('password')
            print('password', password)
            user = authenticate(request, username = username, password = password)
            print('user' , user)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'username or password is incorrct')


    context = {}
    return render(request, 'login.html')


def logoutuser(request):
    print('request', request)
    logout(request)
    return redirect('login')
