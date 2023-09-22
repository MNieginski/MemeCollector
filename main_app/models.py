from django.db import models
from django.urls import reverse

# Create your models here.
class Meme(models.Model):
    title = models.CharField(max_length=25, default='')
    description = models.TextField(max_length=150, default='')
    isFunny = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'meme_id' : self.id})