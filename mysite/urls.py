
    
from django.urls import path
from User import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('otp/', views.otp_fun, name='otp'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('forgot/', views.forgot, name='forgot'),
   
    path('email_otp/', views.email_otp, name='email_otp'),

    path('change_password/', views.change_password, name='change_password'),
    path('change_email/', views.change_email, name='change_email')




]