from django.urls import path
from csk.views import *

app_name='csk'
urlpatterns=[
    path('rayudu/',rayudu,name='rayudu'),
    
]