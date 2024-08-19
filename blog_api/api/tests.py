from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import BlogPost, Tag
from datetime import datetime

# Create your tests here.

today = datetime.now().date()

class BlogPostTests(APITestCase):
    
    def setUp(self):
        # crates 3 posts, with tag 1, tag 2 and both tags
        # they are created with the same date also test the tag creation code
        # where we split the tags 
        self.tag1 = Tag.objects.create(name='django')
        self.tag2 = Tag.objects.create(name='python')
        
        self.blogpost1 = BlogPost.objects.create(
            title = 'post 1', content = 'content 1'
        )
        self.blogpost1.tags.set([self.tag1])

        self.blogpost2 = BlogPost.objects.create(
            title = 'post 2', content = 'content 2'
        )
        self.blogpost2.tags.set([self.tag2])

        self.blogpost3 = BlogPost.objects.create(
            title = 'post 3', content = 'content 3'
        )
        self.blogpost3.tags.set([self.tag1, self.tag2])
    
    def test_get_all_posts(self):
        # test the list view of the api, should return all created posts
        response = self.client.get(reverse('blogposts-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_retrieve_post(self):
        # teste the retrieve view, should return the post with the id passed
        post_id = self.blogpost1.id
        response = self.client.get(reverse('blogposts-detail', args=[post_id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'post 1')
        self.assertEqual(response.data['content'], 'content 1')
        self.assertEqual(response.data['tags_list'][0]['name'], 'django')

    def test_filter_by_dates(self):
        # filter by multiple date formats, should return all 3 posts posted on the date
        # of the tests
        for date_format in ['%Y-%m-%d', '%d-%m-%Y', '%m-%d-%Y']:
            response = self.client.get(reverse('blogposts-list'), {'date': today.strftime(date_format)})
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(len(response.data), 3)

    def test_filter_by_invalid_date(self):
        # puts a invlid date, should return a 400 bad request
        response = self.client.get(reverse('blogposts-list'), {'date': 'd15sa1fsa66511'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_filter_by_tag(self):
        # filter by tag, should return the posts with the tag passed
        response = self.client.get(reverse('blogposts-list'), {'tags': 'python'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_filter_by_date_and_tag(self):
        # filter by tag and date, should return the post with both the tag and the date
        response = self.client.get(reverse('blogposts-list'), {'tags': 'python', 'date': today.strftime('%Y-%m-%d')})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)