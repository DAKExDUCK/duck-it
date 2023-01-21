from django.views.generic import ListView, DetailView

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