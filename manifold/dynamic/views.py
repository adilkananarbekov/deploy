from django.shortcuts import render
from .models import *

def manifold(request):
    logo = Logotype.objects.last()
    testimonials = Testimonials.objects.order_by('-id')[:2]
    return render(request, 'dynamic/footer.html', {'logo':logo, 'testimonials':testimonials})
