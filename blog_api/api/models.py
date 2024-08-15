from django.db import models

# Create your models here.

class BlogPost(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "#{} - {}. Date: {}".format(self.id, self.title, self.date_posted)