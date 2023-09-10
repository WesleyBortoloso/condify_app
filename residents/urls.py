from django.urls import path
from residents.views import index, send_resident_to_supabase

urlpatterns = [
    path('', index),
    path('send_resident/', send_resident_to_supabase, name='send_resident_to_supabase'),
]