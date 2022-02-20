from turtle import title
from django.test import TestCase
from .models import Video

class VideoModelTestCase(TestCase):
    def setUp(self):
        Video.objects.create(title='Video Title')

    
    def test_valid_title(self):
        title = 'Video Title'
        qs = Video.objects.filter(title=title)
        self.assertTrue(qs.exists())
  