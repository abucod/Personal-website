from django.db import models

class About(models.Model):
    name = models.CharField(max_length=250)
    picture = models.ImageField(null=True, blank=True, upload_to=".")
    title = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    phone = models.IntegerField()
    birthday = models.CharField(max_length=100)
    location = models.CharField(max_length=250)
    about_me = models.TextField()

    def __str__(self) :
        return f"{self.name}{self.about_me}"

class Comment(models.Model):
    name = models.CharField(max_length=250)
    picture = models.ImageField(upload_to="./images")
    comentary = models.TextField()

    def __str__(self):
        return self.name

class ClientLogo(models.Model):
    picture = models.ImageField(null=True, blank=True, upload_to="./images")
    url = models.CharField(null=True, blank=True, max_length=250, default="#")

class Education(models.Model):
    name = models.CharField(max_length=250)
    date = models.CharField(max_length=250)
    text = models.TextField()

    def __str__(self):
        return f"{self.name} ::{self.text}"
    
class Experince(models.Model):
    name = models.CharField(max_length=250)
    position = models.CharField(max_length=500)
    date = models.CharField(max_length=250)
    text = models.TextField()

    def __str__(self):
        return f"{self.name} {self.position}"

class Category(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.name}"

class Portfolio(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    picture = models.ImageField(upload_to="./images")
    link = models.CharField(null=True, blank=True, max_length=250, default="#")
    
    def __str__(self):
        return f"{self.name} categry {self.category}"
    
class Skills(models.Model):
    name = models.CharField(max_length=500)
    lavel = models.IntegerField(default=50)

    def __str__(self):
        return f"{self.name} daraja {self.lavel}"

class SocialMedia(models.Model):
    url = models.CharField(max_length=250)
    icon = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.url} {self.url}"
