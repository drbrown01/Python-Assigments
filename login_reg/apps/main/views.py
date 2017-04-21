from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt


# Create your views here.
def index (request):
    return render(request, 'main/index.html')

def login(reaquest):
    if request.method != "POST":
        return redirect  ('/')
    else:
        if request.POST.get('email') == '' or request.POST.get('password') == '':
            messages.error(request, 'Invalid credientials or GTFO!')
            return redirect('/')
    #see if email is in db?
        user = User.objects.filter(email=request.POST.get(email)).first()

    if user and bcrypt.checkpw(request.POST.get('password').encode , user.password.encode()) :
        request.session['user_id'] = user_id
        return redirect('/success')
    else:
        messages.error('GTFO')
        return redirect ('/')
    # if so verify password

def createUser(request):
    if request.method != 'POST':
        return redirect('/')
    else:
        check = User.objects.validateUser(request.POST)
        if check[0] == False:
            for error in check[1]:
                messages.error(request, error)
            return redirect('/')
        else:
             hashed_pw = bcrypt.hashpw(request.POST.get('password').encode(), bcrypt.gensalt())
             user = User.objects.create(
                 name= request.POST.get('name'),
                 email = request.POST.get('email'),
                 password = hashed_pw
                 )
             request.session['user_id'] = user.id
             return redirect('/success')
def success(request):
    return render (request, 'success.html')
