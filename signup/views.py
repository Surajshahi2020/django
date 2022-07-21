from django.shortcuts import render,HttpResponse

from django.template import loader


def login(request):
    return render(request,'login.html',{})

def doLogin(request):
    return render(request,'home.html',{})

def blank(request):
    return render(request,'blank.html',{})

def register(request):
    return render(request,'register.html',{})

def error(request):
    return render(request,'404.html',{})

def forgot_password(request):
    return render(request,'forgot_password.html',{})

    