from django.conf import settings
from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

User = settings.AUTH_USER_MODEL

STATUS = (
    (2,"On Review"),
    (1,"Published"),
    (0,"Draft"),
    (-1,"On Moderation"),
    (-2,"Banned"),
)


class Course(models.Model):
    title = models.CharField(max_length=200, unique=True)
    desc = models.CharField(max_length=2000, default="")

    slug = models.SlugField(null=False, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courses', editable=False)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    views = models.ManyToManyField(User, blank=True, related_name='viewed_by', editable=False)
    likes = models.ManyToManyField(User, blank=True, related_name='liked_by', editable=False)
    saves = models.ManyToManyField(User, blank=True, related_name='saved_by', editable=False)

    def get_views(self):
        return self.views.count()

    def get_likes(self):
        return self.likes.count()
    
    def get_saves(self):
        return self.saves.count()

    def __str__(self) -> str:
        return str(self.slug)


class Lesson(models.Model):
    title = models.CharField(max_length=200)
    body = CKEditor5Field('Text', config_name='extends')

    slug = models.SlugField(null=False, unique=True)
    order = models.PositiveIntegerField(default=None)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    course = models.ForeignKey('Course', on_delete= models.CASCADE, related_name='lessons')

    class Meta:
        ordering = ['order']

    def __str__(self) -> str:
        return str(self.slug)
