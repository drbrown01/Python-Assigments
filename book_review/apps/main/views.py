from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def createUser(request):
    if request.method != 'POST':
        return redirect('/')
    attempt = User.objects.validateUser(request.POST)
    if attempt['status'] == True:
        user = User.objects.createUser(request.POST)
        request.session['user_id'] = user.id
        print (100* '*')
        return redirect('/books')
    else:
        for error in attempt ['errors']:
            messages.add_message(request, messages.ERROR, error, extra_tags="registration")
        return redirect('/')
    #validate the users
def loginUser(request):
    if request.method != 'POST':
        return redirect('/') #Manager Function
    attempt = User.objects.loginUser(request.POST)
    if attempt ['status'] == True:
        request.session['user_id'] = attempt['user'].id
        return redirect('/books')
    else:
        messages.add_message(request, messages.ERROR, attempt['message'], extra_tags="login")
        return redirect('/')
