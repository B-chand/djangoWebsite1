from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("This is homepage of HelloD project. <a href='/admin'>Go to Admin</a>")

def about(request):
    return HttpResponse("This is about page of HelloD project.")

def services(request):
    return HttpResponse("This is services page of HelloD project.")

def contact(request):
    return HttpResponse("This is contact page of HelloD project.")

