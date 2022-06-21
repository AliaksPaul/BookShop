from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include('bookshop.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
