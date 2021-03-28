from django.db import models

# Create your models here.

class NewsModals(models.Model):
    author = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.title
