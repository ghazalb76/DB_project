#django imports
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

#project imports
from .models import User

def users(request):
    users_list = User.objects.all()
    output = ', '.join([u.username for u in users_list])
    return HttpResponse(output)

def signUpResult(request, name):
    response = "You have registered successfully as"
    return HttpResponse(response % name)

def signUp(request):
    return render(request, 'myapp/signUp.html')

def submit_info(request):
    user = User()
    user.name = request.POST.get('name','')
    user.username = request.POST.get('username','')
    user.email = request.POST.get('email','')
    user.password = request.POST.get('password','')
    # user.repass = request.POST.get('repass','')
    user.save()
    return HttpResponse("OK")