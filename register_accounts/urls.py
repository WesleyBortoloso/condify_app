from django.urls import path
from . import views

app_name = 'register_accounts'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('process_form/', views.process_form, name='process_form'),
]