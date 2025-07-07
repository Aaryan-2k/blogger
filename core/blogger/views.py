from django.shortcuts import render,HttpResponse, redirect
from .models import blogs
from django.contrib import messages

# Create your views here.
def home(request):
    return HttpResponse("working ass expected")

def blog_list(request):
    blog_list=blogs.objects.all()
    return render(request,"bloglist.html", {"blogs":blog_list})

def create_blog(request):
    if request.method=="POST":
        try:
            img=request.FILES["blog_image"]
        except Exception as e:
            print(e)
            img=None
        data={"blog_text":request.POST['blog_content'], "blog_title":request.POST['blog_title'],"blog_image":img,"user":request.user}
        blogs.objects.create(**data)
        return redirect("/myblogs/")

    return render(request, "blogcreate.html")

def read_blog(request, id):    
    return render(request, "read.html",{"blog":blogs.objects.get(id=id)})

def update_blog(request, id):
    data=blogs.objects.get(id=id)
    if request.method=="POST":
        try:
            img=request.FILES['blog_image']
        except Exception as e:
            print(e)
            img=None
    
        data.blog_text=request.POST['blog_content']
        data.blog_title=request.POST['blog_title']
        if img:
            data.blog_image=img
        data.save()
        messages.info(request, "Blog has been updated Successfully!")
        return redirect("/myblogs/")
    return render(request,"blogupdate.html", {"blog":data})

def delete_confirm(request, id):
    data=blogs.objects.get(id=id)
    messages.error(request,f'''The blog "{data.blog_title}" has been deleted!''')
    data.delete()
    return redirect("/myblogs/")

def read_myblog(request,id):
    if request.method=='POST':
        pass
    return render(request, "user_read.html", {"blog":blogs.objects.get(id=id)})

def delete_blog_get(request, id):
    data=blogs.objects.get(id=id)
    return render(request, "deleteblog.html",{"blog":data})
def myblogs(request):
    return render(request, "myblogs.html", {"blogs":blogs.objects.filter(user=request.user)})