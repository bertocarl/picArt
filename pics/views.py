from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.http  import HttpResponse


def pics(request):
    return HttpResponse('Welcome to PicArt Website')