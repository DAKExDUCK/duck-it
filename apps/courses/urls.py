from django.urls import path

from .views import CoursesListView, CourseDetailView, LessonView

urlpatterns = [
    path("", CoursesListView.as_view(), name="courses"),
    path("<slug:slug>/", CourseDetailView.as_view(), name="course"),
    path("<slug:slug_course>/lesson/<slug:slug>/", LessonView.as_view(), name="lesson"),
]