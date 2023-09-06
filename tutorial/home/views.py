from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages,sessions
from django.contrib.auth.models import User, auth

from .models import About,Places
#from .forms import Contactform


# Create your views here.
def login_user(request):
    # if 'username' in request.session:
    if  request.user.is_authenticated:
        return redirect('home')
    if request.method =='POST':
        username = request.POST.get('user')
        password = request.POST.get('pass')
        user = authenticate(username=username,password=password)

        if user is not None:
            # request.session['username']= username
            login(request,user)
            return redirect('home')

        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login_user')
            
    else:
        return render(request,'login.html')
@login_required(login_url = '/')
def index(request):
    # if 'username' in request.session:
    # if  request.user.is_authenticated:
    return render(request,'index.html')
    # else: 
    # return render(request, 'login.html')
@login_required(login_url = '/')
def about(request):
    # if 'username' in request.session:
    # if  request.user.is_authenticated:
    dict_ab = {
            'ab': About.objects.all()
                }
    return render(request, 'about.html',dict_ab)
    # else: 
    # return render(request, 'login.html')
@login_required(login_url = '/')
def places(request):
    # if 'username' in request.session: 
    # if  request.user.is_authenticated:
    dict_places = {
                'places': Places.objects.all()
        }        
    return render(request, 'places.html',dict_places)
    # else: 
    # return render(request, 'login.html')
@login_required(login_url = '/')
def logout_user(request):
    # if  request.user.is_authenticated:
    # if 'username' in request.session:
        # request.session.flush()
    logout(request)
    return redirect('login_user')
def register(request):

    # if 'username' in request.session:
    if  request.user.is_authenticated:
        return redirect(home)

    if  request.method == 'POST':
        username= request.POST['username']
        # last_name = request.POST['last_name']
        # username = request.POST['username']
        email =request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if username.strip()=="" or email=="" or password.strip()==" "or confirm_password.strip()=="":
            messages.info(request, 'fill the required fields ')
            return redirect(register)
        elif password==confirm_password:
            
            if  User.objects.filter(username=username).exists():
                messages.info(request, 'username already taken ')
                return redirect(register)
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email is already registered ')
                return redirect(register)

            else:
                user = User.objects.create_user(username=username,
                password=password, email=email)
                user.set_password(password)
                user.save()
                print("success")
                return redirect('login_user')
        else:
            messages.info(request, 'Both passwords are not matching')
            return redirect(register)
    else:
        print("no post method")
        return render(request, 'register.html')
  


