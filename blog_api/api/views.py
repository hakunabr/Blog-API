from django.shortcuts import render
from rest_framework import viewsets
from .models import BlogPost
from .serializers import BlogpostSerializer

# Create your views here.

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogpostSerializer
