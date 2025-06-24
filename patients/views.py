from django.shortcuts import render
from django.http import HttpResponse

def patients(request):
    return HttpResponse("Hello patients")

