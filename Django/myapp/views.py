from django.shortcuts import render

# Create your views here.
def index(request):
    return render (request, "index.html")

def about1(request):
    return render (request, "about.html")

def login(request):
    return render (request, "form.html")
