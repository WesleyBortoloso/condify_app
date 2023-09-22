from django.urls import path
from register_accounts.views import register


urlpatterns = [
    path('', register),
]