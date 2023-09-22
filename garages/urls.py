from django.urls import path
from garages.views import index, send_garage_to_supabase

urlpatterns = [
    path('', index, name="garages_index"),
    path('send_garage/', send_garage_to_supabase, name='send_garage_to_supabase'),
]