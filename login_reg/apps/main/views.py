from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt


# Create your views here.
def index (request):
    return render(request, 'main/index.html')

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
             hashed_pw = bcyrpt.hashpw(request.POST.get('password').encode(), bcrypt.gensalt())
             user = User.objects.create(
                 name= request.POST.get('name'),
                 email = request.POST.get('email'),
                 password = hashed_pw
                 )
             request.session['user_id'] = user.id
             return redirect('/success')
