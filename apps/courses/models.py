from django.db import models
from django.contrib.auth.models import User

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
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courses')
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self) -> str:
        return str(self.slug)


class Lesson(models.Model):
    title = models.CharField(max_length=200)

    slug = models.SlugField(null=False, unique=True)
    order = models.PositiveIntegerField(default=None)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)

    course = models.ForeignKey('Course', on_delete= models.CASCADE, related_name='lessons')

    class Meta:
        ordering = ['order']

    def __str__(self) -> str:
        return str(self.slug)