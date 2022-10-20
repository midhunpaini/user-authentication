from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from signin.models import Signin, Signup
# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password')   
        cpass=request.POST.get('cpassword')
        
        if pass1 == cpass:
            if Signup.objects.filter(username=username).exists():
                messages.error(request, "Username Already exists! Please try someother Username!")
                return redirect('signup')
            
            if Signup.objects.filter(email=email).exists():
                messages.error(request, "Email Already Registered!")
                return redirect('signup')
            
            if len(username)>10:
                messages.error(request, "User name must be under 10 charecters!")
                return redirect('signup')
            
            if pass1 != cpass:
                messages.error(request, "Password Didn't match!")
                return redirect('signup')            
                
                
            if not username.isalnum():
                messages.error(request, "Username must be Alfa-Numeric")  
                return redirect('signup')
        else:
            user=Signup.objects.create(fname=fname,lname=lname,username=username,email=email,password=pass1)        
            user.save()
            return redirect('signin')
        
    return render(request, 'signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('password')
        user= Signup.objects.filter(username=username,password=pass1)
        if user:           
           return render(request, "loggedin.html")  
            
        else:
            print('bad')
            messages.error(request, "Bad Credentials!")
            return redirect('home')
    return render(request, "signin.html")
    

def signout(request):
    return render(request, 'home.html')