from django.shortcuts import render
from rest_framework import viewsets
from datetime import datetime
from .models import BlogPost
from rest_framework.response import Response
from rest_framework import status
from django.utils.timezone import make_aware
from .serializers import BlogpostSerializer
from django.utils.dateparse import parse_date

# Create your views here.

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogpostSerializer

    def list(self, request, *args, **kwargs):
        # implements option to filter by date, first checks if a date is present in the quer params
        date = request.query_params.get('date_posted', None)
        if date:
            # we try to parse the date, to check if it is a valid date
            date = parse_date(date)
            if date:
                # if its valid, we filter the queryset by the date
                first = BlogPost.objects.first()
                queryset = BlogPost.objects.filter(date_posted=date)
            else:
                # if its not valid, we return a 400 Bad Request response
                return Response({"error": "Invalid date format. Please use YYYY-MM-DD"}, status=status.HTTP_400_BAD_REQUEST)
        
        else:
            # if no date is present, return all posts
            queryset = BlogPost.objects.all()
        
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)