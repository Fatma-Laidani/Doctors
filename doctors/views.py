from django.shortcuts import render
from django.http import HttpResponse

def doctors(request):
    return HttpResponse("Hello")


def about_doctor1(request):
    return render(request, 'doctors/doct1.html')
