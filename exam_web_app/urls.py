from django.contrib import admin
from django.urls import path, include
from status.views import status_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', status_view, name='status'),
    path('', include('status.urls')),
]
