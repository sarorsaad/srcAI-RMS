from django.urls import path
from . import views




app_name='radio'
urlpatterns = [
path('', views.homepage, name='homepage'),
path('doctor-dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
path('create-account/', views.create_account_page, name='create_account'),
path('login/', views.login_page, name='login'),

]

