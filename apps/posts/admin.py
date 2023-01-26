from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("slug", "title", "status", "count_of_likes", "count_of_saves")
    
    @admin.display(description='Count of likes')
    def count_of_likes(self, obj: Post):
        return obj.get_count_likes()
    
    @admin.display(description='Count of saves')
    def count_of_saves(self, obj: Post):
        return obj.get_count_saves()
    
    ordering = ('id',)



admin.site.register(Post, PostAdmin)