from datetime import timezone, datetime

from django.db import models


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateField(default=datetime.now)


