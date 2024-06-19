from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def telugu(request):
    return HttpResponse("Hello busy people....!Wellcome To Telugu Industry")
def hindi(request):
    return HttpResponse("Hindi Industry")