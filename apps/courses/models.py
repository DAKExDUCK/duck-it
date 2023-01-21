from django.contrib.auth.models import User
from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


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
    updated_on = models.DateTimeField(auto_now=True, editable=False)
    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    status = models.IntegerField(choices=STATUS, default=0)

    views = models.IntegerField(default=0, editable=False)
    likes = models.IntegerField(default=0, editable=False)

    def __str__(self) -> str:
        return str(self.slug)


class Lesson(models.Model):
    title = models.CharField(max_length=200)
    body = CKEditor5Field('Text', config_name='extends')

    slug = models.SlugField(null=False, unique=True)
    order = models.PositiveIntegerField(default=None)
    updated_on = models.DateTimeField(auto_now=True, editable=False)
    created_on = models.DateTimeField(auto_now_add=True, editable=False)

    course = models.ForeignKey('Course', on_delete= models.CASCADE, related_name='lessons')

    class Meta:
        ordering = ['order']

    def __str__(self) -> str:
        return str(self.slug)
