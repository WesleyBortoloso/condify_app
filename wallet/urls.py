from django.urls import path
from wallet.views import index, send_wallet_to_supabase

urlpatterns = [
    path('', index, name="wallet_index"),
    path('send_wallet/', send_wallet_to_supabase, name='send_wallet_to_supabase'),
]