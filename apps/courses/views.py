from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView
from django.contrib.auth.models import AnonymousUser

from .models import Course, Lesson


class CoursesListView(ListView):
    model = Course
    template_name = "courses/courses_list.html"

    def get_queryset(self):
        return Course.objects.filter(status=1).order_by('likes')


class CourseDetailView(DetailView):
    model = Course
    template_name = "courses/course_detail.html"


class LessonView(DetailView):
    model = Lesson
    template_name = "courses/lesson.html"

    def get_context_data(self, **kwargs):
        context = super(LessonView, self).get_context_data(**kwargs)
        course = Course.objects.get(slug=self.kwargs.get('slug_course'))
        page_alt = course.lessons.get(slug=self.kwargs.get('slug'))
        context['page_alt'] = page_alt
        return context


def like_course(request, slug):
    user = request.user
    if user is AnonymousUser:
        data = {
            'status': 'info',
            'message': 'You must Sign in to use it'
        }
    else:
        course = get_object_or_404(Course, slug=slug, status=1)
        if course.likes.filter(id=user.id).exists():
            course.likes.remove(user)
            data = {
                'status': 'info',
                'message': 'Course unliked'
            }
        else:
            course.likes.add(user)
            data = {
                'status': 'success',
                'message': 'Course liked'
            }
    
    return JsonResponse(data)


def save_course(request, slug):
    user = request.user
    if user is AnonymousUser:
        data = {
            'status': 'info',
            'message': 'You must Sign in to use it'
        }
    else:
        course = get_object_or_404(Course, slug=slug, status=1)
        if course.saves.filter(id=request.user.id).exists():
            course.saves.remove(user)
            data = {
                'status': 'info',
                'message': 'Course removed from Saved'
            }
        else:
            course.saves.add(user)
            data = {
                'status': 'success',
                'message': 'Course added to Saved'
            }
    
    return JsonResponse(data)
