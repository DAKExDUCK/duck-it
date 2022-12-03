from django.urls import path, include

from main_app import views


urlpatterns = [
    path('', views.redirect_page, name='redirect'),
    
    path('about', views.about, name='about'),
    path('home', views.home, name='home'),

    path('contact_us/', include('contact_us.urls')),
    path('accounts/', include('accounts.urls')),
    path('articles/', include('articles.urls')),

    path('admins/', include('admins.urls')),
]
