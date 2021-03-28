from django.shortcuts import render
from .models import NewsModals
# Create your views here.

def Root(request):
    context = {
        "author":"Mohammad Rehbar"
    }
    return render(request,'webapp/index.html',context)

def Home(request):
    return render(request,'webapp/about.html',{})

def Contact(request):
    return render(request,'webapp/contact.html',{})

def News(request):
    obj = NewsModals.objects.all()
    context={
        "data":obj
    }
    return render(request,'webapp/news.html',context)
