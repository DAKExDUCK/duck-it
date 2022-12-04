from django.contrib import admin

from .models import Course, Lesson


class LessonAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("slug", "title", "order", "course")

    ordering = ('-course', '-order')


class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("slug", "title", "count_of_lessons")

    @admin.display(description='Count of lessons')
    def count_of_lessons(self, obj):
        return len(obj.lessons.all())
    
    ordering = ('id',)



admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)