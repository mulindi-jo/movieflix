from turtle import title
from django.db import models

class Video(models.Model):
    title = models.CharField()
    description = models.TextField()
    slug = models.SlugField(blank=True, null=True)
    Video_id = models.CharField()
