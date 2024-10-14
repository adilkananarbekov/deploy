from django.db import models
from django.core.exceptions import ValidationError
import datetime

class Logotype(models.Model):
    logotype = models.ImageField(upload_to='images')
    logotype_footer = models.ImageField(upload_to='images')

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