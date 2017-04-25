from django.shortcuts import render


def index(request):
    return render(request, 'main/index1.html')

def about(request):
    return render(request, 'main/about.html')

def test(request):
    return render(request, 'main/test.html')
    
def pro(request):
    return render(request, 'main/pro.html')
