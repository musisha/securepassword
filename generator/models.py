from django.db import models

# Create your models here.
class Article(models.Model):
    name = models.CharField(max_length=50, blank=False)
    image = models.ImageField(upload_to='generator/images', blank=True)
    body = models.TextField(max_length=1000, blank=False, null=False)
    date = models.DateField()

    def __str__(self):
        return self.name
    