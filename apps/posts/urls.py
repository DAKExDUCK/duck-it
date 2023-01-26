from django.urls import path

from . import views

urlpatterns = [
    path("", views.PostsListView.as_view(), name="posts"),
    path("<slug:slug>/", views.PostDetailView.as_view(), name="post"),
    path('<slug:slug>/like', views.like_post, name="like_post"),
    path('<slug:slug>/save', views.save_post, name="save_post"),
]