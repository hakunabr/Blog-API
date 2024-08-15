from django.test import TestCase
from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import BlogPost

# Create your tests here.

class BlogPostTests(APITestCase):
    
    def setUp(self):
        #create the posts used to test the api
        BlogPost.objects.create(title='Post 1', content='Random Content 1')
        BlogPost.objects.create(title='Post 2', content='Random Content 2')
    
    def test_list_all(self):
        # list all the posts, then tests if the response is 200, and if the number of posts is 2
        url = reverse("blogposts-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_list_posts_by_date(self):
        # list the posts, using a date as filter, tests if status = 200, if one post is returned and if
        # the return post is the correct one
        url = reverse("blogposts-list")
        response = self.client.get(url, {'date_posted': '2024-08-15'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_list_posts_by_invalid_date(self):
        # list the posts, using an invalid date as filter, tests if status = 400
        url = reverse("blogposts-list")
        response = self.client.get(url, {'date_posted': '2uhfashjidsahu'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)