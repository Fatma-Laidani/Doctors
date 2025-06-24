from django.shortcuts import render
from django.http import HttpResponse

def appointments(request):
    return HttpResponse("Hello appointments")

