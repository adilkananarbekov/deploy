from django.shortcuts import render
from .models import *

def manifold(request):
    logo = Logotype.objects.last()
    testimonials = Testimonials.objects.order_by('-id')[:2]
    brands = Brand.objects.order_by('-id')[:6]
    social = SocialMedia.objects.order_by('-id')[:3]
    help_list = HelpList.objects.order_by('-id')[:6]
    care = TakeCare.objects.order_by('-id')[:6]
    if request.method == 'POST':
        email = request.POST.get('email')
        user = Subscribers(email = email)
        user.save()
    return render(request, 'dynamic/footer.html', {'logo':logo, 'testimonials':testimonials, 'brands':brands, 'socials':social, 'help_list':help_list, 'care_list':care})
