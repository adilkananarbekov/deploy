from django.db import models
from django.core.exceptions import ValidationError
import datetime
from django.utils.deconstruct import deconstructible
import os


@deconstructible
class FileExtensionValidator:
    allowed_extensions = ['png', 'jpg', 'jpeg', 'svg']

    def __call__(self, value):
        ext = os.path.splitext(value.name)[1][1:].lower()
        if ext not in self.allowed_extensions:
            raise ValidationError(f'Unsupported file extension. Allowed extensions: {", ".join(self.allowed_extensions)}')


class Logotype(models.Model):
    logotype_in_header = models.FileField(upload_to='images', validators=[FileExtensionValidator()])
    logotype_in_footer = models.FileField(upload_to='images', validators=[FileExtensionValidator()])



class Brand(models.Model):
    title = models.CharField(max_length=30)
    image = models.FileField(upload_to='images', validators=[FileExtensionValidator()])

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
    


class CardSlider(models.Model):
    company_logo = models.FileField(upload_to='images', validators=[FileExtensionValidator()])
    result = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    company = models.CharField(max_length=30)
    product = models.CharField(max_length=20)
    platform = models.CharField(max_length=15)
    card_in_slider = models.FileField(upload_to='images', validators=[FileExtensionValidator()])

    def __str__(self):
        return self.company

def card_slider_view(request):
    cards = CardSlider.objects.all()
    return render(request, 'your_template.html', {'cards': cards})


class Testimonials(models.Model):
    author = models.CharField(max_length=50, default='Unknown')
    publisher = models.CharField(max_length=50, default='Unknown')
    comment = models.TextField(default='Something')

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
    image = models.FileField(upload_to='images', validators=[FileExtensionValidator()])

    def __str__(self):
        return self.title