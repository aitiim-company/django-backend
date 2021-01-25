from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.views.decorators.cache import cache_page

@cache_page(60 * 15)
def hello(request):
    from time import sleep
    sleep(0.5)
    return HttpResponse("hello world")

from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView): # new
    template_name = 'about.html'

from rest_framework import viewsets
from .serializers import HeroSerializer
from .models import Hero

class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer

