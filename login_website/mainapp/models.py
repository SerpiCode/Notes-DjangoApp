from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Notes(models.Model):
    
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    body = models.TextField(max_length=1024)
    date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('notes')