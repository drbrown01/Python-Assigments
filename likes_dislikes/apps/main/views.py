from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt


# Create your views here.
def index (request):
    return render(request, 'main/index.html')

def login(request):
    if request.method != "POST":
        return redirect  ('/')
    else:
        if request.POST.get('email') == '' or request.POST.get('password') == '':
            messages.error(request, 'Invalid credientials or GTFO!')
            return redirect('/')
    #see if email is in db?
        check = User.objects.loginUser(request.POST)
        if check['status']  == False:
            messages.error(request, check[message])
            return redirect('/')
        else:
            request.session['user_id'] = check ['user'].id
            return redirect('/success')

# def createUser(request):
#     if request.method != 'POST':
#        return redirect('/')
#     else:
#
# 		 check = User.objects.validateUser(request.POST)
#
# 		 if check[0] == False:
#
# 			for error in check[1]:
#
# 				messages.error(request, error)
#
# 			return redirect('/')
#
# 		else:
#
# 			#create the user
#
# 			hashed_pw = bcrypt.hashpw(request.POST.get('password').encode(), bcrypt.gensalt())
#
# 			user = User.objects.create(
#
# 				name = request.POST.get('name'),
#
# 				email = request.POST.get('email'),
#
# 				password = hashed_pw
#
# 			)
#
# 			request.session['user_id'] = user.id
#
# 			return redirect('/success')

			#add them to session
#
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
    contex = {
        'post' : Post.objects.all(),
    }
    return render (request, 'main/success.html', context)

def createPost(request):
    if request.method != "POST":
        return redirect('/')
    else:
        # check = check.post.validatePost(request.POST)
        check = Post.objects.validatePost(request.POST)
        if check ['status'] == False:
            for error in check['errors']:
                messages.error(request, error)
            else:
                Post.objects.create(
                    post = request.POST.get('post'),
                    user=User.objects.get(id=request.session['user_id'])    # always shows current user
                )
                return redirect('/success')
