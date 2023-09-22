from django.urls import path
from notifications.views import index, send_notification_to_supabase

urlpatterns = [
    path('', index, name="notifications_index"),
    path('send_notification/', send_notification_to_supabase, name='send_notification_to_supabase'),
]