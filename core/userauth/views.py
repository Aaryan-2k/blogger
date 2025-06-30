from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def register(request):
    if request.method=='POST':
        check=User.objects.filter(username=request.POST['username'])
        if check.exists():
            messages.info(request, "username already taken")
            return redirect('/auth/register/')
        data={"username":request.POST['username'], "email":request.POST['email']}
        print(data)
        user=User(**data)
        user.set_password(request.POST['password'])
        user.save()
        messages.success(request, "account created successfully")
        return redirect('/auth/login/')
    return render(request,"register.html")

def login_page(request):
    if request.method=='POST':
        username=request.POST["username"]
        password=request.POST["password"]
        if not User.objects.filter(username=username).exists():
            messages.warning(request, "invalid username or password")
            return redirect('/auth/login/')
        user=authenticate(username=username, password=password)
        if user==None:
            messages.warning(request, "invalid username or password")
            return redirect('/auth/login/')
        login(request, user)
        return redirect("/list/")
    return render(request,"login.html")

def logout_page(request):
    logout(request)
    return redirect('/auth/login/')