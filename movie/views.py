from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'frontend/index.html', {}) 

def contact(request):
    return render(request, 'frontend/contact.html', {})

def blog(request):
    return render(request, 'frontend/blog.html', {})

def single(request):
    return render(request, 'frontend/single.html', {})
def single2(request):
    return render(request, 'frontend/single2.html', {})
def single3(request):
    return render(request, 'frontend/single3.html', {})
def single4(request):
    return render(request, 'frontend/single4.html', {})
def single5(request):
    return render(request, 'frontend/single5.html', {})
def single6(request):
    return render(request, 'frontend/single6.html', {})


""" def about(request):
    return render(request, 'frontend/about.html', {}) """