from typing_extensions import Required
from django.db import models
from django.db.models.fields import NullBooleanField
from django.utils import timezone
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.name


class Snap(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255, blank=True)
    snap = models.ImageField(upload_to='snaps')# popraw
    date_posted = models.DateTimeField(default=timezone.now)
    tag = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title + ' ' + str(self.date_posted) + ' ' +  str(self.author)



