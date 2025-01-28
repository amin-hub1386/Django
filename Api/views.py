from django.shortcuts import render
from rest_framework import viewsets
from django.views.generic import TemplateView
from Api.models import Post
from Api.serializer import PostSerializer


# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class Home(TemplateView):
    template_name = 'Api/index_page.html'
