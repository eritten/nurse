from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def apply(request):
    return render(request, 'apply.html')

def download(request):
    return render(request, 'download.html')

def detail(request, title, year, month, day):
    pass
