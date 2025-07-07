from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def register(request):
    if request.method=='POST':
        check=User.objects.filter(username=request.POST['username'])
        if check.exists():
            messages.error(request, f'''The username "{request.POST['username']}" has already been taken.''')
            return redirect('/auth/register/')
        data={"username":request.POST['username'], "email":request.POST['email']}
        print(data)
        user=User(**data)
        user.set_password(request.POST['password'])
        user.save()
        messages.success(request, "Your account has been created successfully!")
        return redirect('/auth/login/')
    if request.user.is_authenticated:
        return redirect("/list/")
    return render(request,"register.html")

def login_page(request):
    if request.method=='POST':
        username=request.POST["username"]
        password=request.POST["password"]
        if not User.objects.filter(username=username).exists():
            messages.warning(request, "Invalid Credentials!")
            return redirect('/auth/login/')
        user=authenticate(username=username, password=password)
        if user==None:
            messages.warning(request, "Invalid Credentials!")
            return redirect('/auth/login/')
        login(request, user)
        messages.success(request,f'''Welcome back {user.username}''')
        return redirect("/list/")
    if request.user.is_authenticated:
        return redirect("/list/")
    return render(request,"login.html")

def logout_page(request):
    logout(request)
    messages.info(request, "You have been logged out!")
    return redirect('/auth/login/')