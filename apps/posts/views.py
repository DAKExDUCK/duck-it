from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView

from .models import Post


class PostsListView(ListView):
    model = Post
    template_name = "posts/posts_list.html"

    def get_queryset(self):
        return Post.objects.filter(status=1).order_by('likes')


class PostDetailView(DetailView):
    model = Post
    template_name = "posts/post_detail.html"


def like_post(request, slug):
    user = request.user
    course = get_object_or_404(Post, slug=slug, status=1)
    if course.likes.filter(id=user.id).exists():
        course.likes.remove(user)
        data = {
            'status': 'info',
            'message': 'Post unliked'
        }
    else:
        course.likes.add(user)
        data = {
            'status': 'success',
            'message': 'Post liked'
        }
    
    return JsonResponse(data)


def save_post(request, slug):
    user = request.user
    course = get_object_or_404(Post, slug=slug, status=1)
    if course.saves.filter(id=request.user.id).exists():
        course.saves.remove(user)
        data = {
            'status': 'info',
            'message': 'Post removed from Saved'
        }
    else:
        course.saves.add(user)
        data = {
            'status': 'success',
            'message': 'Post added to Saved'
        }
    
    return JsonResponse(data)
