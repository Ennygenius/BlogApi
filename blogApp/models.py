from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=200)
    body = models.TextField()
    sub_body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    footer = models.CharField(max_length=700)
    reading_time = models.CharField(max_length=255)
    img  = models.ImageField(upload_to='upload', blank=True, null=True)
       

    def __str__(self):
        return self.title

