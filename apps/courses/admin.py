from django.contrib import admin

from .models import Course, Lesson


class LessonAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("slug", "title", "order", "course")

    ordering = ('-course', '-order')


class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("slug", "title", "count_of_lessons", "status", "count_of_likes", "count_of_saves")

    @admin.display(description='Count of lessons')
    def count_of_lessons(self, obj: Course):
        return obj.get_count_lessons()
    
    @admin.display(description='Count of likes')
    def count_of_likes(self, obj: Course):
        return obj.get_count_likes()
    
    @admin.display(description='Count of saves')
    def count_of_saves(self, obj: Course):
        return obj.get_count_saves()
    
    ordering = ('id',)



admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)