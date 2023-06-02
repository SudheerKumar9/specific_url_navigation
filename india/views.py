from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def sachin(request):
    return render(request,'sachin.html')

def third(request):
    return HttpResponse('<center><h1>This is coming from India View Page</h1></center>')