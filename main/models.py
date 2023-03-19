from django.db import models
from django.conf import settings
# About img =======================


class About_img (models.Model):
    img = models.ImageField(upload_to='about/%Y/%m/%d')

    def __str__(self):
        return str(self.img)



# About Text =======================
class About_text (models.Model):
    title = models.CharField(max_length=30,)
    description = models.TextField( max_length=1100)

    def __str__(self):
        return self.title



# About Team =======================
class Our_Team(models.Model):
    img = models.ImageField(upload_to='about/%Y/%m/%d')
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name


class Main(models.Model):
    name_site = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='about/%Y/%m/%d')
    description = models.TextField(max_length=500)
    address = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField()
    facebook = models.URLField()
    twitter = models.URLField()
    whatsapp = models.IntegerField()

    def __str__(self):
        return self.name_site


# Message ========================
class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(max_length=15000)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return f'Message From {self.name}'
