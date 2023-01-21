from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.admin, name='admin_home'),
    path('panel', admin.site.urls),
]