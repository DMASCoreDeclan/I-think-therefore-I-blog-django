from django.shortcuts import render
from django.views import generic
from .models import Post, Comment


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


# class CommentList(generic.ListView):
#     model = Comment