# playground/views.py
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello from index!")

def say_hello(request):
    return HttpResponse("Hello from say_hello!")
