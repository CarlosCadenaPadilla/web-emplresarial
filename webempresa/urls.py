
from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
    # path del core
    path('', include('core.urls')),
    # path del admin
    path('admin/', admin.site.urls),
]

