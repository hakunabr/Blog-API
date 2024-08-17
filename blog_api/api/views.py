from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import BlogPost
from .serializers import BlogpostSerializer
from .filters import BlogPostFilter

# Create your views here.

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogpostSerializer
    filterset_class = BlogPostFilter
    filter_backends = [DjangoFilterBackend]

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('-date_posted')