from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('residents/', include('residents.urls')),
    path('notifications/', include('notifications.urls')),
    path('garages/', include('garages.urls')),
    path('wallet/', include('wallet.urls')),
    path('apartments/', include('apartments.urls')),
    path('', include('home.urls')),
]
