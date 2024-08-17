from django.db import models

# Create your models here.

#apparently id can be omitted, but it's a good practice to include it
class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name='blog_posts')

    def __str__(self):
        return "#{} - {}. Date: {}".format(self.id, self.title, self.date_posted)