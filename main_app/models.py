from django.db import models

# Create your models here.
class Meme(models.Model):
    title = models.CharField(max_length=25, default='')
    description = models.TextField(max_length=150, default='')
    isFunny = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title} ({self.id})'