from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hai(request):
    return HttpResponse('<h1><marquee>hi sanju ur crush is starring at u</marquee>0</h1>')