from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(blank=False, null=False, max_length=100)
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)
    img = models.ImageField(upload_to='media/')
    content = models.TextField(blank=True)

    def __str__(self):
        return self.title
