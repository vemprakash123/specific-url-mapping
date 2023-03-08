from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def virat(request):
    return HttpResponse('<h1><marquee>virat is best batsman</marquee></h1>')
def raina(request):
    return HttpResponse('<h1><marquee>raina is good ipl player</marquee></h1>')