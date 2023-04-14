from django.shortcuts import redirect, render
from .models import *
from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def todolist(request):  
    task = Task.objects.all()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form= TodoForm
    context={'task':task,'form':form}
    return render(request,'tem/home.html',context)

@login_required(login_url='login')
def updateitem(request,pk):
    item = Task.objects.get(id=pk)
    form = TodoForm(instance=item)
    if request.method == "POST":
        form = TodoForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('/')
    context ={'item':item,'form':form}
    return render(request,'tem/update.html',context)

@login_required(login_url='login')
def deleteitem(request,pk):
    item = Task.objects.get(id=pk)
    if request.method == "POST":
        item.delete()
        return redirect('/')
    context = {'item':item}
    return render(request,'tem/delete.html',context)


def register(request):
    if request.method == "POST":
        myform = UserForm(request.POST)
        if myform.is_valid():
            myform.save()
            return redirect('login')
    else:
        myform = UserForm
    context = {'myform':myform}
    return render(request,'tem/register.html',context)


def userlogin(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request , username=username , password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
    context={}
    return render(request,'tem/login.html',context)

@login_required(login_url='login')
def userlogout(request):
    logout(request)
    return redirect('login')