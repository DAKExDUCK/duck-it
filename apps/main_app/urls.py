from django.urls import path, include

from main_app import views


urlpatterns = [
    path('', views.redirect_page, name='redirect'),
    
    path('about', views.about, name='about'),
    path('home', views.home, name='home'),

    path('login/', views.login_signup, name='login'),
    path('', include('accounts.urls')),

    path('courses/', include('courses.urls')),
    path('posts/', include('posts.urls')),

    path('admins/', include('admins.urls')),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
]
