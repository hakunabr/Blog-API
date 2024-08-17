from django_filters import rest_framework as filters
from .models import BlogPost
from django.core.exceptions import ValidationError
from datetime import datetime

class BlogPostFilter(filters.FilterSet):
    # crate the available filters to be used to query the api
    tags = filters.CharFilter(field_name= 'tags__name',lookup_expr='icontains')
    date = filters.DateFilter(field_name= 'date_posted', lookup_expr='gte', input_formats=['%Y-%m-%d', '%d-%m-%Y', '%m-%d-%Y'])

    class Meta:
        model = BlogPost
        fields = ['tags', 'date']