#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from .forms import AddForm
import socket
import time

# Create your views here.
name=socket.gethostname()
def index(request):
    return HttpResponse(u"welcome to my test page!")
answer="stop"
def input(request):
    global answer
    if request.method == 'POST':

        answer=request.POST['laomao']
        
        if answer == "up":
            print("car is up")
        if answer == "down":
            print("car is down")
       #  form= AddForm(request.POST)
       #  if form.is_valid():
       #     c=form.POST['hello']
       #     #a=form.cleaned_data['a']
       #     #b=form.cleaned_data['b']
       #     #answer =str(int(a)+int(b))
       #     answer=c
       
            
        return render(request,'home.html',{'host_name':name,'answer':answer}) 
           # return HttpResponse(str(int(a)+int(b)))
    else:
        form =AddForm()

    return render(request,'home.html',{'host_name':name,'form':form,'answer':answer}) 



