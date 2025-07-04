from django.urls import path
from .import views


urlpatterns=[
    path('',views.home,name='home'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/add_doctor/', views.add_doctor, name='add_doctor'),
    path('dashboard/all_doctors/', views.all_doctors, name='all_doctors'),
    path('doctors/edit/<int:doctor_id>/', views.edit_doctor, name='edit_doctor'),
    path('doctors/delete/<int:doctor_id>/', views.delete_doctor, name='delete_doctor'),
    path('doctors/<int:doctor_id>/', views.doctor_detail, name='doctor_detail'),

]