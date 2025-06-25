from django.shortcuts import render,redirect
# from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # يمكن تغييره إلى صفحة أخرى
        else:
            messages.error(request, 'اسم المستخدم أو كلمة المرور غير صحيحة')
    return render(request, 'dashboard/login.html')

def home(request):
    return render(request,'dashboard/home.html')


def dashboard(request):
    return render(request,'dashboard/dashboard.html')

