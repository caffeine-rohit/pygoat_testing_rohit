from django.db import models
from django.conf import settings

class Blogs(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    blog_id = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.blog_id
