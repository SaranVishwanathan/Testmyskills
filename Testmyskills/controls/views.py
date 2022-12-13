from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

def registration(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']

        user= User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password1)
        user.save()
        return redirect('/Login')

    else:
        return render(request, 'register.html')

def Login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        
        if user is not None:
            auth.login(request,user)
            #return HttpResponse('login sucess')
            return render(request,'home.html')
    else:
        return render(request,'Login.html')

def logout(request):
    auth.logout(request)
    return redirect('/Login')

def About(request):
    return render(request,'About.html')

def Contact(request):
    return render(request,'Contact.html')

def Test(request):
    return render(request,'Test.html')

def level_1(request):
    return render(request,'level_1.html')

def level_2(request):
    return render(request,'level_2.html')

def level_3(request):
    return render(request,'level_3.html')

def level_4(request):
    return render(request,'level_4.html')

def level_5(request):
    return render(request,'level_5.html')





