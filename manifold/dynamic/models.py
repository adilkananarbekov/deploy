from django.db import models
from django.core.exceptions import ValidationError
import datetime

class Logotype(models.Model):
    logotype = models.ImageField(upload_to='images')
    logotype_footer = models.ImageField(upload_to='images')



class Brand(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title
    

class HelpList(models.Model):
    title = models.CharField(max_length=30)
    we_help = models.TextField()

    def __str__(self):
        return self.title

    def clean(self):
        if len(self.we_help) > 70:
            raise ValidationError('Не превышать 70 символов')
        

class TakeCare(models.Model):
    take_care = models.CharField(max_length=15)

    def __str__(self):
        return self.take_care
    



class Testimonials(models.Model):
    author = models.CharField(max_length=50, default='Unknown')
    publisher = models.CharField(max_length=50, default='Unknown')
    comment = models.TextField(default='Something')
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.author

    def clean(self):
        if len(self.comment) > 250:
            raise ValidationError('Комментарий не должен превышать 250 символов')
        


class Subscribers(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email
        


class SocialMedia(models.Model):
    title = models.CharField(max_length=30)
    link = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.title