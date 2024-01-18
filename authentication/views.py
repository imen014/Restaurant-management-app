from django.shortcuts import render, redirect, get_object_or_404
from authentication.forms import UserAppCreationForm
from django.contrib.auth import login, logout, authenticate
from authentication.forms import LoginForm
from authentication.models import UserAppModel

from django.contrib.auth.decorators import login_required


def create_user(request):
    user_form = UserAppCreationForm()
    message = ''
    if request.method == "POST":
        user_form = UserAppCreationForm(request.POST, request.FILES)
        if user_form.is_valid():
            user_form.save()
            message = "user created"
            return redirect('login_user')
        else:
            message = "check data"

    return render(request, 'authentication/user_created.html', {'user_form':user_form, 'message':message})


def login_user(request):  
    login_form = LoginForm()
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            email = login_form.cleaned_data['email']
            password = login_form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home', id=user.id)
    return render(request, 'authentication/login.html', {'login_form':login_form})

@login_required
def home(request, id):
    user = get_object_or_404(UserAppModel, id=id)
    return render(request, 'authentication/home.html', {'user':user})

@login_required
def delete_users(request):
    users = UserAppModel.objects.all()
    users.delete()
    return redirect('get_users')


@login_required
def get_users(request):
    users = UserAppModel.objects.all()
    return render(request, 'authentication/get_users.html', {'users':users})


def logout_user(request):
    logout(request)
    return redirect('login_user')

@login_required
def update_user(request, id):
    message = 'check data'
    user_instance = get_object_or_404(UserAppModel, id=id)
    form_user = UserAppCreationForm(instance=user_instance)
    if request.method == "POST":
        form_user = UserAppCreationForm(request.POST, request.FILES, instance=user_instance)
        if form_user.is_valid():
            form_user.save()
            message = 'user updated'
            return redirect('login_user')
    return render(request, 'authentication/user_modified.html', {'form_user':form_user, 'message':message, 'user_instance':user_instance})


@login_required
def show_my_account(request, id):
    user = get_object_or_404(UserAppModel, id=request.user.id)
    return render(request, 'authentication/show_account.html', {'user':user})

@login_required
def detele_my_account(request, id):
    account = get_object_or_404(UserAppModel, id=request.user.id)
    account.delete()
    return redirect('login_user')

    

