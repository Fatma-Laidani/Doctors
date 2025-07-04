from django.shortcuts import render,redirect
# from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import DoctorForm
from doctors.models import Doctor
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required



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


def logout_view(request):
  logout(request) # يقوم بإزالة جلسة المستخدم (user session)
  return redirect('home')  # إعادة التوجيه لصفحة تسجيل الدخول أو أي صفحة أخرى


def home(request):
    return render(request,'dashboard/home.html')



@login_required(login_url='login')
def dashboard(request):
    return render(request,'dashboard/dashboard.html')
       
  



@login_required(login_url='login')
def add_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ تم إضافة الطبيب بنجاح")
            return redirect('add_doctor')  # أو صفحة النجاح
        else:
            # print(form.errors)  # ← سيعرض الأخطاء في التيرمنال
            messages.error(request, "❌ تحقق من صحة البيانات")
    else:
        form = DoctorForm()

    return render(request, 'dashboard/add_doctor.html', {'form': form})




@login_required(login_url='login')
def all_doctors(request):
    doctors =Doctor.objects.all()
    return render(request, 'dashboard/all_doctors.html', {'doctors': doctors})

@login_required(login_url='login')
def edit_doctor(request, doctor_id):
    doctor = Doctor.objects.get(id=doctor_id)
    if request.method == 'POST':
        form = DoctorForm(request.POST, request.FILES, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('all_doctors')
    else:
        form = DoctorForm(instance=doctor)
    return render(request, 'dashboard/edit_doctor.html', {'form': form, 'doctor': doctor})


@login_required(login_url='login')
def delete_doctor(request, doctor_id):
    doctor = Doctor.objects.get(id=doctor_id)
    doctor.delete()
    return redirect('all_doctors')
