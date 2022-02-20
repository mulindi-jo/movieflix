from turtle import title
from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    Video_id = models.CharField(max_length=100)
