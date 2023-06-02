from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def rayudu(request):
    return render(request,'rayudu.html')

def second(request):
    return HttpResponse('<center><h1>This is coming from Csk View Page</h1></center>')