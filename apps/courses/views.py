from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView

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


def like_course(request, pk):
    course = get_object_or_404(Course, id=request.POST.get('course_slug'))
    if course.likes.filter(id=request.user.id).exists():
        course.likes.remove(request.user)
        messages.add_message(request, messages.info, 'Course inliked')
    else:
        course.likes.add(request.user)
        messages.add_message(request, messages.success, 'Course liked')


def favorite_course(request, pk):
    user = request.user
    course = get_object_or_404(Course, id=request.POST.get('course_slug'))
    if user.favorites.filter(slug=course.slug).exists():
        user.favorites.remove(favorite)
        messages.add_message(request, messages.info, 'Course inliked')
    else:
        user.favorites.add(favorite)
        messages.add_message(request, messages.success, 'Course liked')

    if request.method == 'POST':
        favorite = Course.objects.get(pk=pk)
        user = request.user
        user.favorites.add(favorite)
        messages.add_message(request, messages.success, 'Course added to Saved')