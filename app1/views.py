from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def dhoni(request):
    return HttpResponse('<h1>MSD is my favourate cricketer..')
def abd(request):
    return HttpResponse('<h1>ABD is known as MR.360</h1>')