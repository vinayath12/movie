from django.db import models

# Create your models here.
class Movie(models.Model):
    name=models.CharField(max_length=250)
    des=models.TextField()
    rating=models.FloatField()
    image=models.ImageField(upload_to='gallery')