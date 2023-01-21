from django.urls import path

from . import views

urlpatterns = [
    path("", views.CoursesListView.as_view(), name="courses"),
    path("<slug:slug>/", views.CourseDetailView.as_view(), name="course"),
    path("<slug:slug_course>/lesson/<slug:slug>/", views.LessonView.as_view(), name="lesson"),
    path('blogpost-like/<int:pk>', views.like_course, name="like_course"),
]