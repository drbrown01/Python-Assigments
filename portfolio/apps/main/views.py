from django.shortcuts import render, redirect

# Create your views here.
def testimonials(request):
    return render(request, 'main/testimonials.html')

def index(request):
    return render(request, 'main/index.html')

def test(request):
    return render(request, 'main/test.html')

def create(request):
    print (request.method)
    if request.method == 'POST':
        print(100* "*")
        print(request.POST)
        print(100* "*")
        request.session['name'] = request.POST['first_name']
        return redirect ('/')
    else:
        return redirect('/')
