from django.urls import path
from .import views

urlpatterns=[
    path('doctors/',views.doctors,name='doctors'),
    path('doct1/', views.about_doctor1, name='doct1'),
]