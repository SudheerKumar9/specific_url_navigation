from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def bumrah(request):
    return render(request,'bumrah.html')

def first(request):
    return HttpResponse('<center><h1>This response is coming from Mumbai Page</h1</center>')