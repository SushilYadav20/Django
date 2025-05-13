from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib import messages

# Create your views here.

def base(request):
    return render(request,'hotelapp/base.html')


def home(request):
    return render(request,'hotelapp/home.html')

def layout(request):
    return render(request,'layout.html')

def register(request):
    if request.method == 'POST':
        username =  request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password != confirm_password:
            messages.error(request,'Password and confirm password must be same')
        if User.objects.filter(username=username).exists():
            messages.error(request,"Username already taken!")

        #if User.objects.filter(email=email).exists():
            #messages.error("Email already registered!")
        else:
            User.objects.create_user(username=username , password=password)
            #User.save()
            messages.success(request,'Registration successful.Please login')
            return redirect('/login/')
            
    return render(request,'hotelapp/reg.html')

def login(request):
    return render(request,'hotelapp/login.html')

def blog(request):
    if request.method == 'GET':
        return render(request,'hotelapp/blog.html')
    if request.method == 'POST':
        data = request.POST
        title = data.get('title')
        description = data.get('des')   # here des is my input box name come from ui side
        blog_status = data.get('status')
        mobile_number = data.get('mobile')
        # to print this use 
        print(title,description,blog_status,mobile_number,'dgdhs')

        Blog.objects.create(title=title,des=description,status= blog_status,mobile=mobile_number)

        return redirect('/list_blog/')

def list_blog(request):
    data = Blog.objects.all()
    message = request.GET.get('message')
    print(message,'hjdjh')
    return render(request,'hotelapp/list_blog.html',{'blog_data':data,'message':message})

def Cards(request):
    data = Blog.objects.all()
    return render(request,'hotelapp/cards.html',{'blog_data':data})

def student(request):
    if request.method == 'GET':
        return render(request,'hotelapp/student.html')
    if request.method == 'POST':
        return render(request,'hotelapp/student.html')
    
def update_blog(request,id):
    if request.method == 'GET' :
        update_data = Blog.objects.filter(id=id)
        if not update_data:
            data = Blog.objects.all()
            message = 'id not found'
            return render(request,'hotelapp/list_blog.html',{'message':message,'blog_data':data})
        #for autofill
        update_data = Blog.objects.get(id=id)
        return render(request,'hotelapp/update_blog.html',{'Update_data':update_data})

    if request.method == 'POST':
        update_blog = Blog.objects.get(id=id)
        # if not update_blog:
        #     message = 'id not found'
        #     return render(request,'hotelapp/update_blog.html',{'message':message})
        title=request.POST.get('title')
        desc=request.POST.get('des')
        Status=request.POST.get('status')
        Contact=request.POST.get('mobile')

        update_blog.title=title
        update_blog.des=desc
        update_blog.status=Status
        update_blog.mobile=Contact
        update_blog.save()
        return redirect('/list_blog/')
    
def delete_blog(request,id):
    user_data=Blog.objects.filter(id=id)
    if not user_data:
        data=Blog.objects.all()
        message="id not found"
        return render(request,'hotelapp/list_blog.html',{'message':message,'blog_data':data })
    user_data = Blog.objects.get(id=id)

    # user_data.delete()
    message = 'data deleted'
    return redirect('/list_blog/?message=datadeleted')
        

def todo(request):
    if request.method == 'GET':
     return render(request,'hotelapp/todo.html')
    if request.method == 'POST':
        data=request.POST
        task=data.get('task')
        Todo.objects.create(task=task)
        return render(request,'hotelapp/todo.html')
    

def show_todo(request):
    data = Todo.objects.all()
    return render(request,'hotelapp/show_todo.html',{'data':data})

def update_todo(request,id):
    if request.method == 'GET':
        update_data=Todo.objects.filter(id=id)
        if not update_data:
            message="id not found"
            return render(request,'hotelapp/update_todo.html',{'message':message})
        update_data=Todo.objects.get(id=id)
        return render(request,'hotelapp/update_todo.html',{'update_data':update_data})
    if request.method == 'POST':
        update_data=Todo.objects.filter(id=id)
        if not update_data:
            message="id not found"
            return render(request,'hotelapp/update_todo.html',{'message':message})
        update_data=Todo.objects.get(id=id)
        task = request.POST.get('task')

        update_data.task=task
        update_data.save()
        return redirect('/show_todo/',{'update_data':update_data})

def delete_todo(request,id):
    if request.method == 'GET':
        update_data=Todo.objects.filter(id=id)
        if not update_data:
            message='id not found'
            return redirect('/update_todo/?message=idnotfound')
        update_data=Todo.objects.get(id=id)
        update_data.delete()
        message='data deleted'
        return redirect('/show_todo/?message=datadeleted')
    
def vinay(request):
    return redirect('/user_blog/')
