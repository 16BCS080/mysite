from django.db import models

# Create your models here.

class posts(models.Model):
    title=models.CharField(max_length=200)
    cost=models.CharField(max_length=200)
    description=models.TextField()
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural="posts"
    