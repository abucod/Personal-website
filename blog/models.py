from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    date = models.DateField()
    text = models.TextField()
    picture = models.ImageField(upload_to="./images")

    def __str__(self):
        return self.title