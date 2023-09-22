from django.urls import path
from apartments.views import index, send_apartment_to_supabase

urlpatterns = [
    path('', index, name='apartments_index'),
    path('send_apartment/', send_apartment_to_supabase, name='send_apartment_to_supabase'),
]
