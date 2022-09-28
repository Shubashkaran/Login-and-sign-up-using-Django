from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == "POST":
        fn = request.POST['first_name']
        ln = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']

        if pass1==pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already exits")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email already used")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=pass1,email=email,first_name=fn,last_name=ln)
                user.save()
                return redirect('login')
        else:
            messages.info(request, "password not matching")
            return redirect('register')
        return redirect('/')
    else:
        return render(request,'register.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['password']
        user = auth.authenticate(username=username, password=pass1)
        if(user is not None):
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"invalid credentials")
            return redirect("login")
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')