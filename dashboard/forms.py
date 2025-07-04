from django import forms
from doctors.models import Doctor

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'
        labels = {
            'name': 'الاسم الكامل',
            'specialty': 'التخصص',
            'phone': 'رقم الهاتف',
            'email': 'البريد الإلكتروني',
            'photo': 'صورة الطبيب',
            'bio'  :'إضافة',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', }),
            'specialty': forms.TextInput(attrs={'class': 'form-control',}),
            'phone': forms.TextInput(attrs={'class': 'form-control', }),
            'email': forms.EmailInput(attrs={'class': 'form-control', }),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control form-control-sm',}) ,
            'bio'  : forms.Textarea(attrs={'class': 'form-control','rows': 4,}),
        }
