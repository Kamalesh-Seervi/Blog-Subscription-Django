from django.shortcuts import render,redirect
from . forms import UserCreationForm, CreateUserForm
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login


def home(request):
    return render(request, 'account/index.html')


def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'RegisterForm': form}
    return render(request, 'account/register.html', context)


def my_login(request):
    form = AuthenticationForm()

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # from data i getting the username and passsworf we have over rided the username to email but in forms i cant override the syntx but in email only
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_writer == True:
                login(request, user)
                return redirect('writer_dashboard')
            if user is not None and user.is_writer == False:
                login(request, user)
                return redirect('client_dashboard')

    context = {'Login': form}
    return render(request, 'account/login.html',context)
