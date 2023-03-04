from django.db import models
from django.urls import reverse

# Create your models here.

class Job(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    date = models.DateTimeField()
    image = models.ImageField(upload_to='images')
    def get_absolute_url(self):
        return reserve('job', args=(self.pk, self.title, self.date.year, self.date.month, self.date.day))
